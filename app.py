from flask import Flask, render_template, request, session
import os

from modules.aritmatika import *
from modules.logika import *
from modules.transformasi import *

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))
app.secret_key = os.environ.get("SECRET_KEY", "kalkulator-secret-key-2024")

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []
    history = session["history"]
    hasil = None
    if request.method == "POST":

        if request.form.get("action") == "clear_history":
            session["history"] = []
            return render_template("index.html", hasil=None, history=history)

         # Hapus satu item riwayat berdasarkan indeks
        if request.form.get("action") == "delete_one":
            try:
                idx = int(request.form.get("delete_index", -1))
                if 0 <= idx < len(history):
                    if hasil:
                        history.append(hasil)
                        session["history"] = history
                        session.modified = True
            except (ValueError, IndexError):
                pass
            return render_template("index.html", hasil=None, history=history)


        angka1 = request.form.get("angka1", "")
        angka2 = request.form.get("angka2", "")

        # INPUT ANGKA 1
        if angka1 != "":
            try:
                f1 = float(angka1)
                if f1.is_integer():
                    angka1 = int(f1)
                else:
                    angka1 = f1
                val1 = float(angka1)
                angka1 = int(val1) if val1.is_integer() else val1
            except ValueError:
                pass # Tetap sebagai string (contoh untuk Heksa)
        else:
            angka1 = 0

        # INPUT ANGKA 2
        if angka2 != "":
            try:
                f2 = float(angka2)
                if f2.is_integer():
                    angka2 = int(f2)
                else:
                    angka2 = f2
                val2 = float(angka2)
                angka2 = int(val2) if val2.is_integer() else val2
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
            session["history"] = history
            session.modified = True

    return render_template(
        "index.html",
        hasil=hasil,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)