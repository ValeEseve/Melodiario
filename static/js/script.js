document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("navbar-toggle");
    const menu = document.getElementById("navbar-default");

    if (toggleButton && menu) {
        toggleButton.addEventListener("click", () => {
            menu.classList.toggle("hidden");
            menu.classList.toggle("flex"); 
        });
    }
});