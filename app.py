from flask import Flask, render_template, request

from modules.aritmatika import *
from modules.logika import *
from modules.transformasi import *


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    hasil = None
    history = []

    if request.method == "POST":

        angka1 = request.form.get("angka1", "")
        angka2 = request.form.get("angka2", "")

        # INPUT ANGKA 1
        if angka1 != "":
            angka1 = float(angka1)
        else:
            angka1 = 0

        # INPUT ANGKA 2
        if angka2 != "":
            angka2 = float(angka2)
        else:
            angka2 = 0

        operasi = request.form["operasi"]

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

        #Logika    
        elif operasi == "and":
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

        #Transformasi
        elif operasi == "biner":
            hasil = desimal_ke_biner(angka1)

        elif operasi == "oktal":
            hasil = desimal_ke_oktal(angka1)

        elif operasi == "heksa":
            hasil = desimal_ke_heksa(angka1)

        elif operasi == "desimal":
            hasil = biner_ke_desimal(str(int(angka1)))

        elif operasi == "celcius_ke_fahrenheit":
            hasil = celcius_ke_fahrenheit(angka1)

        elif operasi == "celcius_ke_kelvin":
            hasil = celcius_ke_kelvin(angka1)

        elif operasi == "celcius_ke_reamur":
            hasil = celcius_ke_reamur(angka1)

        elif operasi == "idr_ke_usd":
            hasil = idr_ke_usd(angka1)

        elif operasi == "idr_ke_eur":
            hasil = idr_ke_eur(angka1)

        elif operasi == "idr_ke_sgd":
            hasil = idr_ke_sgd(angka1)

    history.append(hasil)

    return render_template("index.html",hasil=hasil,history=history )

if __name__ == "__main__":
    app.run(debug=True)