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

- Nombre: **Nataniel Ricardo Alarcon Aduviri**
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

- `index.html` → Página principal; estilos en `assets/css/style.css` y comportamiento en `assets/js/main.js`
- `robots.txt` → Instrucciones para buscadores
- `sitemap.xml` → Mapa del sitio
- No necesita base de datos ni servidor.

---

Hecho con ❤️ para Orbisoft · La Paz, Bolivia


## Control de Gastos — páginas informativas

Sección independiente en `control-de-gastos/`: presentación (`index.html`),
privacidad (`privacidad.html`) y condiciones (`condiciones.html`).
Reutiliza los tokens y el logo de BRAND.md; `site.css` limita sus reglas a
`.expense-site`. No altera el menú ni la página principal y no distribuye APK.
Las páginas funcionan sin JavaScript y contienen enlaces recíprocos y contacto.

Las declaraciones se contrastaron con LocalService, DriveBackupService y la
configuración de fuentes de la app el 10 de octubre de 2026. Mantenerlas
actualizadas cuando cambie el tratamiento de datos. Desconectar cierra sesión;
revocar permisos y eliminar respaldos son operaciones independientes.

### Comprobar y publicar

Servir la raíz con `python -m http.server 8080` y abrir
`http://localhost:8080/control-de-gastos/`. Revisar también las dos páginas
legales, sus enlaces y la presentación en móvil antes de publicar.

GitHub Pages continúa sirviendo la raíz del repositorio. Para Cloudflare Pages,
importar este mismo repositorio, elegir la rama que se quiera publicar, sin
framework ni compilación y con la raíz como directorio de salida del sitio.
Revisar qué archivos de la raíz serán públicos antes del despliegue: el
repositorio contiene también documentos y un ZIP previo; no añadir secretos.
Ningún despliegue, commit o push forma parte de estos cambios locales.

Las URLs canónicas y sitemap conservan `https://benitoscam.github.io/Orbisoft/`.
Si se elige otra dirección principal, actualizar las canónicas, og:url,
sitemap y robots.txt de forma coordinada.

URLs previstas de la app una vez publicados estos cambios:
- https://benitoscam.github.io/Orbisoft/control-de-gastos/
- https://benitoscam.github.io/Orbisoft/control-de-gastos/privacidad.html
- https://benitoscam.github.io/Orbisoft/control-de-gastos/condiciones.html

Publicar estas páginas no confirma la aprobación de OAuth. Revisar el estado
de Google Cloud y sus requisitos con las URLs definitivas. Drive se describe
en pruebas hasta que el propietario confirme su cambio a producción.
