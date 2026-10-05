# Orbisoft Design System

Sistema de diseño unificado para los SaaS de **Orbisoft**.

Todos tus sistemas (inventario, clínicas, laboratorios, servicios...) comparten
el mismo estilo → se ven como **una suite de productos de la misma empresa**.

---

## 📁 Archivos

| Archivo | Descripción |
|---------|-------------|
| `design-system.css` | Variables + componentes (botones, inputs, cards, tablas, navbar, sidebar, login) |
| `login.html` | **Login A** — versión CSS puro (sin dependencias), usa `design-system.css` |
| `login-stitch.html` | **Login B** — diseño generado por Stitch, usa Tailwind CSS (CDN) |
| `dashboard.html` | Ejemplo de dashboard con sidebar, stats y tabla |
| `DESIGN.md` | Documentación completa de todos los componentes |

### Comparación de logins

| | `login.html` | `login-stitch.html` |
|---|---|---|
| Estilos | CSS puro (`design-system.css`) | Tailwind CSS (CDN) |
| Internet | ✅ Funciona offline | ⚠️ Requiere internet |
| Personalización | Editando variables CSS | Editando clases Tailwind |
| Visual | Muy parecido | Más detallado (grid, glows) |

> **Tip:** Ambos comparten la misma estructura split-screen y la marca Orbisoft.
> Usa `login.html` si quieres control total sin dependencias, o `login-stitch.html`
> como referencia visual de mayor detalle.

---

## 🚀 Cómo usarlo en tu SaaS

### 1. Copia los archivos a tu proyecto

```
tu-saas/
├── css/
│   └── design-system.css    ← copiar aquí
├── login.html
└── index.html
```

### 2. Importa el CSS en tu HTML

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link
  href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
  rel="stylesheet"
/>
<link rel="stylesheet" href="css/design-system.css" />
```

### 3. Usa las clases

```html
<button class="orb-btn orb-btn-primary">Guardar</button>

<div class="orb-card">
  <div class="orb-card-title">Mi tarjeta</div>
</div>

<div class="orb-stat">
  <div class="orb-stat-label">Ventas</div>
  <div class="orb-stat-value">Bs 1.250</div>
</div>
```

📖 **Lista completa de componentes:** ver [`DESIGN.md`](DESIGN.md)

---

## 🎨 Personalización por SaaS

Cada sistema puede variar el acento sin perder la identidad Orbisoft:

```css
/* En el CSS o en un <style> extra */
:root {
  /* Dental SaaS */
  --orb-blue: #0d5c75;   /* teal clínico */

  /* Inventario SaaS (default) */
  /* --orb-blue: #00a3ff; */

  /* Clínicas SaaS */
  /* --orb-blue: #14b8a6; */
}
```

✅ **Mantén siempre:** fondo `#0a0a0a`, tarjetas `#141414`, tipografía Inter, logo Orbisoft.

---

## 🖼️ Vista previa

Abre `login.html`, `login-stitch.html` o `dashboard.html` en tu navegador para ver los ejemplos.

```bash
# Opcional: servidor local
npx serve .
```

---

## 📌 Reglas de marca

1. **Logo**: siempre el cubo 3x3 (plata + azul) + texto `ORBISOFT`
2. **Tipografía**: Inter en todos los textos
3. **Fondo oscuro** en todos los sistemas
4. **Botón primario** siempre en el color de acento
5. **Footer**: © 2026 Orbisoft · La Paz, Bolivia

---

Hecho con ❤️ para Orbisoft · La Paz, Bolivia
