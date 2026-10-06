# Orbisoft — Página Web

Página web estática de Orbisoft. Lista para desplegar en **GitHub Pages** (gratis).

## Cómo subirla a GitHub Pages (5 minutos)

### 1. Crear repositorio en GitHub

1. Entra a [github.com](https://github.com) e inicia sesión.
2. Clic en **New repository**.
3. Nombre recomendado: `orbisoft` o `orbisoft-web`.
4. Déjalo **público**.
5. No marques "Add a README".
6. Crea el repositorio.

### 2. Subir los archivos

Puedes hacerlo de dos formas:

**Opción A — Desde la web de GitHub (más fácil)**

1. Entra al repositorio vacío.
2. Clic en **uploading an existing file**.
3. Arrastra el archivo `index.html` (y este README si quieres).
4. Escribe un mensaje de commit (ej: "Primera versión de la web") y sube.

**Opción B — Con Git (si ya sabes usarlo)**

```bash
git init
git add .
git commit -m "Primera versión de la web de Orbisoft"
git branch -M main
git remote add origin https://github.com/Benitoscam/orbisoft.git
git push -u origin main
```

### 3. Activar GitHub Pages

1. En tu repositorio ve a **Settings** → **Pages**.
2. En "Source" elige **Deploy from a branch**.
3. Branch: `main` / carpeta: `/ (root)`.
4. Guarda.
5. En 1-2 minutos tendrás tu URL pública:
   **https://benitoscam.github.io/Orbisoft/**

## Datos ya actualizados

- Nombre: **Natanei Ricardo Alarcon Aduviri**
- WhatsApp: **+591 705 61683**
- Correo: **orbisoftapps@gmail.com**

## Formulario (Formspree)

El formulario ya está preparado. Solo falta activarlo:

1. Ve a [formspree.io](https://formspree.io) y crea una cuenta gratis.
2. Crea un nuevo formulario.
3. Copia el endpoint (ejemplo: `https://formspree.io/f/xpwkgqyz`).
4. Abre `index.html` y reemplaza `YOUR_FORM_ID` por el código que te den.
5. Guarda y vuelve a subir el archivo.

El formulario ya incluye:

- Asunto personalizado del correo
- Campo para poder responder directo al cliente
- Protección anti-spam (honeypot)

## SEO Local incluido

- Title y description optimizados para “software La Paz / Bolivia”
- Open Graph + Twitter Cards
- Schema.org LocalBusiness (datos estructurados)
- Geo-tags (La Paz, Bolivia)
- robots.txt + sitemap.xml
- NAP consistente en footer (Nombre, WhatsApp, Email)

## Estructura

- `index.html` → Toda la página (HTML + CSS + JS embebido)
- `robots.txt` → Instrucciones para buscadores
- `sitemap.xml` → Mapa del sitio
- No necesita base de datos ni servidor.

---

Hecho con ❤️ para Orbisoft · La Paz, Bolivia
