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


/* =========================
   PILIH OPERASI
========================= */

const operationButtons = document.querySelectorAll(".op-btn");

const operasiInput = document.getElementById("operasiInput");

const selectedText = document.getElementById("selectedText");

operationButtons.forEach(button => {

    button.addEventListener("click", () => {

        operationButtons.forEach(btn => {
            btn.classList.remove("selected");
        });

        button.classList.add("selected");

        const operasi = button.dataset.operasi;

        operasiInput.value = operasi;

        selectedText.innerHTML = operasi.toUpperCase();

    });

});


/* =========================
   VALIDASI
========================= */

const form = document.getElementById("calcForm");

form.addEventListener("submit", (e) => {

    if(operasiInput.value === ""){

        e.preventDefault();

        alert("Pilih operasi terlebih dahulu!");

    }

});

/* =========================
   INPUT DINAMIS
========================= */

const angka2Input = document.getElementById("angka2");

operationButtons.forEach(button => {

    button.addEventListener("click", () => {

        const operasi = button.dataset.operasi;

        /*
            OPERASI 1 INPUT
        */

        if(
            operasi === "akar" ||
            operasi === "faktorial" ||
            operasi === "fibonacci" ||
            operasi === "not" ||
            operasi === "biner" ||
            operasi === "oktal" ||
            operasi === "heksa" ||
            operasi === "desimal" ||
            operasi === "fahrenheit" ||
            operasi === "kelvin" ||
            operasi === "reamur" ||
            operasi === "usd" ||
            operasi === "eur" ||
            operasi === "sgd"
        ){

            angka2Input.style.display = "none";

            angka2Input.removeAttribute("required");

            angka2Input.value = "";

        }

        /*
            OPERASI 2 INPUT
        */

        else{

            angka2Input.style.display = "block";

            angka2Input.setAttribute("required", true);

        }

    });

});