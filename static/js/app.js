const toggle = document.getElementById("navToggle");
const nav = document.querySelector(".nav");

if (toggle && nav) {
    toggle.addEventListener("click", () => {
        nav.classList.toggle("nav--open");
    });
}
