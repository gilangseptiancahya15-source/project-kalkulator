const themeToggle = document.getElementById("themeToggle");

/* =========================
   LOAD THEME
========================= */

if(localStorage.getItem("theme") === "light"){

    document.body.classList.add("light-mode");

    themeToggle.innerHTML = "☀️";

}

/* =========================
   TOGGLE THEME
========================= */

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("light-mode");

    /*
        LIGHT MODE
    */

    if(document.body.classList.contains("light-mode")){

        localStorage.setItem("theme", "light");

        themeToggle.innerHTML = "☀️";

    }

    /*
        DARK MODE
    */

    else{

        localStorage.setItem("theme", "dark");

        themeToggle.innerHTML = "🌙";

    }

});