from flask import Flask, render_template, request

from modules.aritmatika import *
from modules.logika import *
from modules.transformasi import *

app = Flask(__name__)

# HISTORY GLOBAL
history = []


@app.route("/", methods=["GET", "POST"])
def index():

    hasil = None

    if request.method == "POST":

        angka1 = request.form.get("angka1", "")
        angka2 = request.form.get("angka2", "")

        # INPUT ANGKA 1
        if angka1 != "":
            try:
                angka1 = float(angka1)
            except ValueError:
                pass # Tetap sebagai string (contoh untuk Heksa)
        else:
            angka1 = 0

        # INPUT ANGKA 2
        if angka2 != "":
            try:
                angka2 = float(angka2)
            except ValueError:
                pass
        else:
            angka2 = 0

        operasi = request.form["operasi"]

        # =========================
        # ARITMATIKA
        # =========================

        if operasi == "tambah":
            hasil = tambah(angka1, angka2)

        elif operasi == "kurang":
            hasil = kurang(angka1, angka2)

        elif operasi == "kali":
            hasil = kali(angka1, angka2)

        elif operasi == "bagi":
            hasil = bagi(angka1, angka2)

        elif operasi == "modulus":
            hasil = modulus(angka1, angka2)

        elif operasi == "pangkat":
            hasil = pangkat(angka1, angka2)

        elif operasi == "akar":
            hasil = akar(angka1)

        elif operasi == "floor":
            hasil = floor_division(angka1, angka2)

        elif operasi == "faktorial":
            hasil = faktorial(angka1)

        elif operasi == "fibonacci":
            hasil = fibonacci(angka1)

        # =========================
        # LOGIKA
        # =========================

        elif operasi in ["and", "or", "not", "xor", "nand", "nor"]:

            # VALIDASI INPUT 0 DAN 1

            if angka1 not in [0, 1]:

                hasil = {
                    "hasil": "Error",
                    "rumus": "Logika",
                    "langkah": "Input hanya boleh 0 atau 1"
                }

            elif operasi != "not" and angka2 not in [0, 1]:

                hasil = {
                    "hasil": "Error",
                    "rumus": "Logika",
                    "langkah": "Input hanya boleh 0 atau 1"
                }

            else:

                if operasi == "and":
                    hasil = operasi_and(bool(angka1), bool(angka2))

                elif operasi == "or":
                    hasil = operasi_or(bool(angka1), bool(angka2))

                elif operasi == "not":
                    hasil = operasi_not(bool(angka1))

                elif operasi == "xor":
                    hasil = operasi_xor(bool(angka1), bool(angka2))

                elif operasi == "nand":
                    hasil = operasi_nand(bool(angka1), bool(angka2))

                elif operasi == "nor":
                    hasil = operasi_nor(bool(angka1), bool(angka2))

        # =========================
        # TRANSFORMASI FLEKSIBEL
        # =========================
        elif operasi.startswith("trans_"):
            parts = operasi.split("_")
            kategori = parts[1]
            dari = parts[2]
            ke = parts[4]

            if kategori == "bilangan":
                hasil = konversi_bilangan(str(angka1), dari, ke)
            elif kategori == "suhu":
                hasil = konversi_suhu(angka1, dari, ke)
            elif kategori == "uang":
                hasil = konversi_mata_uang(angka1, dari, ke)

        # SIMPAN HISTORY
        if hasil:
            history.append(hasil)

    return render_template(
        "index.html",
        hasil=hasil,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)