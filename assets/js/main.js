/* Orbisoft — Comportamiento principal */

// Cerrar menú móvil al hacer clic en un enlace
document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    document.querySelector(".nav-links").classList.remove("active");
  });
});

/* ============================================================
   Animaciones de scroll (reveal)
   - Los elementos con clase .reveal aparecen al entrar en pantalla
   - Usa IntersectionObserver: no altera el rendimiento en scroll
   ============================================================ */
(function initReveal() {
  const items = document.querySelectorAll(".reveal");

  // Sin soporte o sin JS: mostrar todo inmediatamente
  if (!("IntersectionObserver" in window) || items.length === 0) {
    items.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          // Deja de observar: la animación ocurre una sola vez
          obs.unobserve(entry.target);
        }
      });
    },
    {
      // Empieza cuando el elemento está al 80% de la altura visible
      threshold: 0.15,
      // Margen para que dispare un poco antes de entrar al viewport
      rootMargin: "0px 0px -60px 0px",
    }
  );

  items.forEach((el) => observer.observe(el));
})();
