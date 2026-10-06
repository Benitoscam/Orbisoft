"""
Genera el og-image.jpg (1200x630) de Orbisoft a partir del logo SVG oficial.

Uso:
    python scripts/generate_og_image.py

Salida:
    og-image.jpg   (raiz del proyecto, listo para GitHub Pages)
"""

import math
import os
import re

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------- config
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_PATH = os.path.join(ROOT, "assets", "logo", "orbisoft-mark.svg")
OUT_PATH = os.path.join(ROOT, "og-image.jpg")

W, H = 1200, 630

BG = (10, 10, 10)            # #0a0a0a
CARD = (20, 20, 20)          # #141414
BLUE = (0, 163, 255)         # #00a3ff
SILVER = (200, 200, 200)     # #c8c8c8
TEXT = (245, 245, 245)       # #f5f5f5
MUTED = (160, 160, 160)      # #a0a0a0
BORDER = (42, 42, 42)        # #2a2a2a

FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_SEMI = r"C:\Windows\Fonts\seguisb.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_MONO = r"C:\Windows\Fonts\consola.ttf"


def hex_to_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(len(a)))


def over(fg, bg, alpha):
    """Mezcla fg sobre bg con opacidad alpha -> color RGB opaco.
    ImageDraw NO compone alpha en RGBA, asi que pre-mezclamos."""
    return tuple(int(round(bg[i] + (fg[i] - bg[i]) * alpha)) for i in range(3))


# ------------------------------------------------------------ SVG parsing
def parse_svg(path):
    """Devuelve (polygons, orbit_ellipse, front_path) del mark de Orbisoft."""
    with open(path, "r", encoding="utf-8") as fh:
        svg = fh.read()

    polys = []
    for m in re.finditer(r"<polygon\s+points=\"([^\"]+)\"\s+fill=\"([^\"]+)\"", svg):
        pts = [tuple(float(v) for v in p.split(",")) for p in m.group(1).split()]
        polys.append((pts, hex_to_rgb(m.group(2))))

    ell = re.search(
        r"<ellipse\s+cx=\"([\d.]+)\"\s+cy=\"([\d.]+)\"\s+rx=\"([\d.]+)\"\s+ry=\"([\d.]+)\""
        r"\s+transform=\"rotate\((-?[\d.]+)\s+[\d.]+\s+[\d.]+\)\"",
        svg,
    )
    ellipse = (
        float(ell.group(1)), float(ell.group(2)),
        float(ell.group(3)), float(ell.group(4)), float(ell.group(5)),
    ) if ell else None

    path_m = re.search(r'<path d="([^"]+)"', svg)
    front = None
    if path_m:
        # "M x,y C x,y x,y x,y C x,y x,y x,y" -> 14 coordenadas (2 segmentos cubicos)
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", path_m.group(1))]
        front = [
            # segmento 1: p0 (M) + 3 puntos de control
            ((nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5]), (nums[6], nums[7])),
            # segmento 2: arranca en el final del anterior
            ((nums[6], nums[7]), (nums[8], nums[9]), (nums[10], nums[11]), (nums[12], nums[13])),
        ]
    return polys, ellipse, front


# --------------------------------------------------------------- geometry
def bezier(p0, p1, p2, p3, steps=60):
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out


def ellipse_points(cx, cy, rx, ry, rot_deg, steps=720):
    """Puntos de una elipse rotada (SVG: angulo 0 en el extremo derecho)."""
    rot = math.radians(rot_deg)
    pts = []
    for i in range(steps + 1):
        a = 2 * math.pi * i / steps
        x, y = rx * math.cos(a), ry * math.sin(a)
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot),
                    cy + x * math.sin(rot) + y * math.cos(rot)))
    return pts


def dashed_subpaths(points, dash, gap):
    """Aplica patron de guiones (dasharray SVG) a una polilinea cerrada."""
    visible, current, acc, on = [], [], 0.0, True
    total = len(points)
    for i in range(total):
        p, q = points[i], points[(i + 1) % total]
        d = math.hypot(q[0] - p[0], q[1] - p[1])
        if d == 0:
            continue
        remaining, t = d, 0.0
        while remaining > 1e-9:
            need = (dash if on else gap) - acc
            take = min(need, remaining)
            t1 = t + take / d
            visible.append((p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t,
                            p[0] + (q[0] - p[0]) * t1, p[1] + (q[1] - p[1]) * t1, on))
            t = t1
            acc += take
            remaining -= take
            if acc >= (dash if on else gap) - 1e-9:
                acc = 0.0
                on = not on

    # agrupa segmentos visibles consecutivos en polilineas
    for x1, y1, x2, y2, vis in visible:
        if vis:
            if current:
                current.append((x2, y2))
            else:
                current = [(x1, y1), (x2, y2)]
        elif current:
            if len(current) > 1:
                yield current
            current = []
    if len(current) > 1:
        yield current


# ----------------------------------------------------------------- layout
def draw_tracked_text(draw, xy, text, font, fill, tracking=0.0, anchor="la"):
    """Dibuja texto con letter-spacing (tracking en px)."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill, anchor=anchor)
        x += draw.textlength(ch, font=font) + tracking
    return x - tracking


def text_width(draw, text, font, tracking=0.0):
    if not text:
        return 0.0
    return sum(draw.textlength(c, font=font) for c in text) + tracking * (len(text) - 1)


def radial_glow(img, center, radius, color, alpha):
    """Capa de resplandor radial suave."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, cy = center
    steps = 60
    for i in range(steps, 0, -1):
        t = i / steps
        r = radius * t
        a = int(alpha * (1 - t) ** 2)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (a,))
    layer = layer.filter(ImageFilter.GaussianBlur(40))
    img.alpha_composite(layer)


def main():
    polys, ellipse, front = parse_svg(SVG_PATH)

    # ---- canvas base
    img = Image.new("RGBA", (W, H), BG + (255,))

    # resplandores de marca
    radial_glow(img, (300, 300), 520, BLUE, 90)
    radial_glow(img, (1180, 640), 420, BLUE, 45)

    # borde interior sutil
    frame = ImageDraw.Draw(img)
    frame.rounded_rectangle([28, 28, W - 28, H - 28], radius=26, outline=BORDER, width=2)

    # ---- marca (cubo en orbita) --------------------------------------
    SX, SY = 0, 0          # offset del viewBox 240x180
    SCALE = 300 / 240.0    # mark de 300px de ancho
    MARK_X, MARK_Y = 96, 168

    def tp(p):
        return (MARK_X + (p[0] - SX) * SCALE, MARK_Y + (p[1] - SY) * SCALE)

    # capa de brillo para la orbita
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)

    # orbita trasera (guiones) detras del cubo
    if ellipse:
        cx, cy, rx, ry, rot = ellipse
        pts = [tp(p) for p in ellipse_points(cx, cy, rx, ry, rot)]
        for sub in dashed_subpaths(pts, dash=140 * SCALE, gap=300 * SCALE):
            col = lerp(BLUE, SILVER, 0.15) + (140,)
            for i in range(len(sub) - 1):
                gd.line([sub[i], sub[i + 1]], fill=col, width=4)

    # capa del cubo (detrás de la orbita frontal)
    cube = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(cube)
    for pts, fill in polys:
        cd.polygon([tp(p) for p in pts], fill=fill + (255,), outline=BG, width=3)

    # orbita frontal con gradiente azul -> plata
    if front:
        seg = bezier(*front[0]) + bezier(*front[1])[1:]
        seg = [tp(p) for p in seg]
        n = len(seg) - 1
        for i in range(n):
            t = i / n
            col = lerp(BLUE, SILVER, max(0.0, (t - 0.45) / 0.35)) if t > 0.45 else BLUE
            gd.line([seg[i], seg[i + 1]], fill=col + (255,), width=4)
        last = seg[-1]
    else:
        last = None

    # particula / satelite
    if last:
        sx, sy = last
        gd.ellipse([sx - 11, sy - 11, sx + 11, sy + 11], outline=BLUE + (150,), width=2)
        gd.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=BLUE + (255,))

    glow_blur = glow.filter(ImageFilter.GaussianBlur(7))
    img.alpha_composite(glow_blur)
    img.alpha_composite(glow)
    img.alpha_composite(cube)

    # ---- divisor vertical (pre-mezclado: ImageDraw no compone alpha)
    div = ImageDraw.Draw(img)
    for i in range(H - 280):
        t = i / (H - 280)
        a = (1 - abs(t - 0.5) * 2) ** 0.6
        div.line([(470, 140 + i), (471, 140 + i)], fill=over(BORDER, BG, 0.3 + 0.7 * a))

    # ---- bloque de texto ------------------------------------------------
    draw = ImageDraw.Draw(img)

    # badge
    badge_font = ImageFont.truetype(FONT_MONO, 16)
    badge_txt = "LA PAZ · BOLIVIA"
    bw = text_width(draw, badge_txt, badge_font, tracking=2.2)
    bx, by = 530, 176
    div.rounded_rectangle([bx - 18, by - 13, bx + bw + 18, by + 31], radius=20,
                          fill=over(BLUE, BG, 0.13), outline=over(BLUE, BG, 0.55), width=1)
    draw_tracked_text(draw, (bx, by), badge_txt, badge_font, (104, 196, 255), tracking=2.2)

    # wordmark
    word_font = ImageFont.truetype(FONT_BOLD, 82)
    word_y = 236
    wx = draw_tracked_text(draw, (530, word_y), "ORBISOFT", word_font, TEXT, tracking=23)
    # punto de acento
    dot_r = 9
    div.ellipse([wx + 34 - dot_r, word_y + 66 - dot_r, wx + 34 + dot_r, word_y + 66 + dot_r],
                fill=BLUE)

    # tagline
    tag_font = ImageFont.truetype(FONT_REG, 30)
    draw.text((532, 372), "Software y sistemas claros,", font=tag_font, fill=MUTED)
    draw.text((532, 412), "modulares y a medida.", font=tag_font, fill=MUTED)

    # URL / CTA
    url_font = ImageFont.truetype(FONT_SEMI, 24)
    url_txt = "benitoscam.github.io/Orbisoft"
    url_w = text_width(draw, url_txt, url_font, tracking=0.6)
    uy = 476
    div.rounded_rectangle([530, uy, 530 + url_w + 44, uy + 52], radius=12,
                          fill=over(BLUE, BG, 0.13), outline=over(BLUE, BG, 0.55), width=1)
    draw_tracked_text(draw, (552, uy + 13), url_txt, url_font, (104, 196, 255), tracking=0.6)

    # ---- guardar
    out = img.convert("RGB")
    out.save(OUT_PATH, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"OK -> {OUT_PATH} ({os.path.getsize(OUT_PATH) / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
