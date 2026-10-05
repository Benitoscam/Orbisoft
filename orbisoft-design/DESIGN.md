# Orbisoft Design System — Documentación

Sistema de diseño unificado para todos los SaaS de **Orbisoft**.
Objetivo: que todos los sistemas se vean como una **suite de productos de la misma empresa**.

---

## 🎨 Colores

| Token | Valor | Uso |
|-------|-------|-----|
| `--orb-bg` | `#0a0a0a` | Fondo principal |
| `--orb-bg-soft` | `#0f0f0f` | Fondos secundarios |
| `--orb-card` | `#141414` | Tarjetas |
| `--orb-card-hover` | `#1a1a1a` | Tarjetas al hover |
| `--orb-border` | `#2a2a2a` | Bordes |
| `--orb-text` | `#f5f5f5` | Texto principal |
| `--orb-muted` | `#a0a0a0` | Texto secundario |
| `--orb-dim` | `#666666` | Texto deshabilitado |
| `--orb-silver` | `#c8c8c8` | Logo / acentos |
| **`--orb-blue`** | **`#00a3ff`** | **Acento principal** |
| `--orb-teal` | `#0d5c75` | Acento secundario (marca) |
| `--orb-success` | `#22c55e` | Éxito |
| `--orb-warning` | `#f59e0b` | Advertencia |
| `--orb-danger` | `#ef4444` | Error / peligro |

### Uso del acento
- **Azul `#00a3ff`**: botones primarios, links, estados activos, foco
- **Teal `#0d5c75`**: panel de marca del login, acentos secundarios

---

## 🔤 Tipografía

- **Fuente:** Inter (Google Fonts)
- **Mono:** JetBrains Mono / Fira Code (números, códigos)

| Clase | Tamaño | Uso |
|-------|--------|-----|
| `.orb-h1` | clamp(2rem → 3.2rem) | Titular principal |
| `.orb-h2` | clamp(1.5rem → 2.2rem) | Títulos de sección |
| `.orb-h3` | 1.25rem | Subtítulos |
| `.orb-small` | 0.875rem | Texto pequeño |
| `.orb-muted` | — | Texto secundario |

---

## 🧩 Componentes

### Botones

```html
<button class="orb-btn orb-btn-primary">Principal</button>
<button class="orb-btn orb-btn-secondary">Secundario</button>
<button class="orb-btn orb-btn-ghost">Fantasma</button>
<button class="orb-btn orb-btn-danger">Peligro</button>

<!-- Tamaños -->
<button class="orb-btn orb-btn-primary orb-btn-sm">Pequeño</button>
<button class="orb-btn orb-btn-primary orb-btn-lg">Grande</button>
<button class="orb-btn orb-btn-primary orb-btn-block">Ancho completo</button>
```

### Campos de formulario

```html
<div class="orb-field">
  <label class="orb-label" for="email">Correo</label>
  <input class="orb-input" type="email" id="email" placeholder="tu@empresa.com" />
  <p class="orb-hint">Texto de ayuda</p>
</div>

<!-- Con icono -->
<div class="orb-input-icon">
  <span class="orb-icon">🔍</span>
  <input class="orb-input" type="search" placeholder="Buscar..." />
</div>

<!-- Textarea y select -->
<textarea class="orb-textarea" placeholder="Mensaje"></textarea>
<select class="orb-select"><option>Opción</option></select>
```

### Badges

```html
<span class="orb-badge orb-badge-blue">Azul</span>
<span class="orb-badge orb-badge-success">Activo</span>
<span class="orb-badge orb-badge-warning">Pendiente</span>
<span class="orb-badge orb-badge-danger">Cancelado</span>
<span class="orb-badge orb-badge-neutral">Neutro</span>

<!-- Con punto brillante -->
<span class="orb-badge orb-badge-success"><span class="orb-dot"></span> En vivo</span>
```

### Cards

```html
<div class="orb-card">Contenido</div>
<div class="orb-card orb-card-interactive">Con hover</div>
<div class="orb-card orb-card-flat">Fondo suave</div>

<div class="orb-card">
  <div class="orb-card-header">
    <span class="orb-card-title">Título</span>
    <a href="#">Ver más →</a>
  </div>
  ...
</div>
```

### Stat cards (KPIs)

```html
<div class="orb-stat">
  <div class="orb-stat-label">Ventas del mes</div>
  <div class="orb-stat-value">Bs 48.250</div>
  <div class="orb-stat-delta up">▲ +12.4%</div>
</div>
```

### Tablas

```html
<div class="orb-table-wrap">
  <table class="orb-table">
    <thead>
      <tr><th>Columna</th><th style="text-align:right">Total</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>Dato</td>
        <td class="num" style="text-align:right">Bs 1.250</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Alertas

```html
<div class="orb-alert orb-alert-info">ℹ️ Información</div>
<div class="orb-alert orb-alert-success">✅ Éxito</div>
<div class="orb-alert orb-alert-warning">⚠️ Advertencia</div>
<div class="orb-alert orb-alert-danger">❌ Error</div>
```

### Navbar

```html
<nav class="orb-navbar">
  <div class="orb-navbar-inner">
    <a href="#" class="orb-logo">
      <div class="orb-logo-mark">
        <span></span><span></span><span></span>
        <span></span><span></span><span></span>
        <span></span><span></span><span></span>
      </div>
      ORBISOFT
    </a>
    <ul class="orb-nav-links">
      <li><a href="#" class="active">Inicio</a></li>
      <li><a href="#">Servicios</a></li>
      <li><a href="#">Contacto</a></li>
    </ul>
  </div>
</nav>
```

### Sidebar + Layout

```html
<div class="orb-layout">
  <aside class="orb-sidebar">
    <a href="#" class="orb-logo">...</a>
    <div class="orb-sidebar-section">General</div>
    <a href="#" class="orb-sidebar-link active">📊 Dashboard</a>
    <a href="#" class="orb-sidebar-link">📦 Inventario</a>
  </aside>
  <main class="orb-main">
    ...
  </main>
</div>
```

---

## 📐 Layout

```html
<!-- Contenedor centrado -->
<div class="orb-container">...</div>

<!-- Sección con padding -->
<section class="orb-section">...</section>

<!-- Grids responsivos -->
<div class="orb-grid orb-grid-2">2+ columnas</div>
<div class="orb-grid orb-grid-3">3+ columnas</div>
<div class="orb-grid orb-grid-4">4+ columnas</div>
```

---

## 🔧 Utilidades

| Clase | Función |
|-------|---------|
| `.orb-flex` | Flex container |
| `.orb-flex-between` | Space-between centrado |
| `.orb-flex-center` | Centrar contenido |
| `.orb-gap` / `.orb-gap-sm` | Espaciado 1rem / 0.5rem |
| `.orb-mt` / `.orb-mt-lg` | Margen superior 1rem / 2rem |
| `.orb-mb` | Margen inferior 1rem |
| `.orb-text-center` | Texto centrado |
| `.orb-mono` | Fuente monoespaciada |

---

## 📱 Responsive

- **≥ 900px**: sidebar visible, login en 2 columnas
- **< 900px**: sidebar oculta, login en 1 columna
- **< 768px**: nav-links ocultas, grids se apilan
