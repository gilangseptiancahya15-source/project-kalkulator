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

        const allSelects = document.querySelectorAll(".op-select");
        if (allSelects) {
            allSelects.forEach(s => s.selectedIndex = 0);
        }

        button.classList.add("selected");

        const operasi = button.dataset.operasi;

        operasiInput.value = operasi;

        selectedText.innerHTML = operasi.toUpperCase();

    });

});

/* =========================
   SUB MENU TRANSFORMASI
========================= */

const transformButtons =
    document.querySelectorAll(".transform-btn");

const transformContents =
    document.querySelectorAll(".transform-content");

transformButtons.forEach(button => {

    button.addEventListener("click", () => {

        transformButtons.forEach(btn => {
            btn.classList.remove("active");
        });

        button.classList.add("active");

        const target = button.dataset.transform;

        transformContents.forEach(content => {
            content.classList.remove("active");
        });

        document
            .getElementById(target)
            .classList.add("active");

    });

});


/* =========================
   SUB-TABS TRANSFORMASI & DROPDOWN
========================= */

const subTabBtns = document.querySelectorAll('.sub-tab-btn');
const transformCategories = document.querySelectorAll('.transform-category');

function updateTransformValue(catId) {
    const catDiv = document.getElementById(catId);
    if (!catDiv) return;
    
    const selFrom = catDiv.querySelector('.op-select-from');
    const selTo = catDiv.querySelector('.op-select-to');
    
    if (selFrom && selTo) {
        const catName = selFrom.dataset.cat;
        const operasi = `trans_${catName}_${selFrom.value}_ke_${selTo.value}`;
        
        operasiInput.value = operasi;
        selectedText.innerHTML = `${selFrom.options[selFrom.selectedIndex].text} &rarr; ${selTo.options[selTo.selectedIndex].text}`;
        
        const angka2Input = document.getElementById("angka2");
        if (angka2Input) {
            angka2Input.style.display = "none";
            angka2Input.removeAttribute("required");
            angka2Input.value = "";
        }
        
        const logicInputs = document.querySelectorAll(".logic-input");
        logicInputs.forEach(input => {
            input.removeAttribute("min");
            input.removeAttribute("max");
            input.placeholder = "Masukkan angka";
        });
    }
}

subTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        subTabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        transformCategories.forEach(cat => cat.style.display = 'none');
        const targetId = btn.dataset.target;
        document.getElementById(targetId).style.display = 'block';
        
        document.querySelectorAll(".op-btn").forEach(btn => {
            btn.classList.remove("selected");
        });
        
        updateTransformValue(targetId);
    });
});

const transformSelects = document.querySelectorAll('.op-select-from, .op-select-to');
transformSelects.forEach(select => {
    select.addEventListener('change', (e) => {
        document.querySelectorAll(".op-btn").forEach(btn => {
            btn.classList.remove("selected");
        });
        const cat = e.target.dataset.cat;
        updateTransformValue(`cat-${cat}`);
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

/* =========================
   VALIDASI INPUT LOGIKA
========================= */

const logicInputs = document.querySelectorAll(".logic-input");

operationButtons.forEach(button => {

    button.addEventListener("click", () => {

        const operasi = button.dataset.operasi;

        /*
            MENU LOGIKA
        */

        if(
            operasi === "and" ||
            operasi === "or" ||
            operasi === "not" ||
            operasi === "xor" ||
            operasi === "nand" ||
            operasi === "nor"
        ){

            logicInputs.forEach(input => {

                input.setAttribute("min", "0");
                input.setAttribute("max", "1");

                input.placeholder = "Masukkan 0 atau 1";

            });

        }

        /*
            MENU SELAIN LOGIKA
        */

        else{

            logicInputs.forEach(input => {

                input.removeAttribute("min");
                input.removeAttribute("max");

                input.placeholder = "Masukkan angka";

            });

        }

    });

});

