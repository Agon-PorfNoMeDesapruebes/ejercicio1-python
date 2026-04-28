// Obtener elementos
const boton = document.getElementById("navToggle");
const menu = document.getElementById("navMenu");

// Evento click
boton.addEventListener("click", () => {
    menu.classList.toggle("active");
});