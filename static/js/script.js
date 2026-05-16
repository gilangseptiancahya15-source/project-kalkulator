const menuButtons = document.querySelectorAll(".menu-btn");

const menuContents = document.querySelectorAll(".menu-content");

menuButtons.forEach(button => {

    button.addEventListener("click", () => {

        menuButtons.forEach(btn => {
            btn.classList.remove("active");
        });

        button.classList.add("active");

        const target = button.dataset.menu;

        menuContents.forEach(content => {
            content.classList.remove("active");
        });

        document.getElementById(target).classList.add("active");

    });

});