/* Orbisoft — Comportamiento principal */
/* Generado desde index.html */

// Cerrar menú móvil al hacer clic en un enlace
document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    document.querySelector(".nav-links").classList.remove("active");
  });
});
