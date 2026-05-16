def desimal_ke_biner(angka):
    hasil = bin(int(angka))

    return {
        "hasil": hasil,
        "rumus": "Decimal → Binary",
        "langkah": f"{angka} dikonversi menjadi {hasil}"
    }

def desimal_ke_oktal(angka):
    hasil = oct(int(angka))

    return {
        "hasil": hasil,
        "rumus": "Decimal → Octal",
        "langkah": f"{angka} dikonversi menjadi {hasil}"
    }

def desimal_ke_heksa(angka):
    hasil = hex(int(angka))

    return {
        "hasil": hasil,
        "rumus": "Decimal → Hexadecimal",
        "langkah": f"{angka} dikonversi menjadi {hasil}"
    }

def biner_ke_desimal(angka):
    hasil = int(angka, 2)

    return {
        "hasil": hasil,
        "rumus": "Binary → Decimal",
        "langkah": f"{angka} dikonversi menjadi {hasil}"
    }

# KONVERSI SUHU
def celcius_ke_fahrenheit(c):
    hasil = (c * 9/5) + 32

    return {
        "hasil": hasil,
        "rumus": "(C × 9/5) + 32",
        "langkah": f"{c}°C menjadi {hasil}°F"
    }

def celcius_ke_kelvin(c):
    hasil = c + 273.15

    return {
        "hasil": hasil,
        "rumus": "C + 273.15",
        "langkah": f"{c}°C menjadi {hasil}K"
    }

def celcius_ke_reamur(c):
    hasil = c * 4/5

    return {
        "hasil": hasil,
        "rumus": "C × 4/5",
        "langkah": f"{c}°C menjadi {hasil}°R"
    }

# KONVERSI MATA UANG
def idr_ke_usd(idr):

    rate = 16000

    hasil = idr / rate

    return {
        "hasil": round(hasil, 2),
        "rumus": "IDR ÷ 16000",
        "langkah": f"{idr} IDR menjadi ${round(hasil,2)}"
    }

def idr_ke_eur(idr):

    rate = 17500

    hasil = idr / rate

    return {
        "hasil": round(hasil, 2),
        "rumus": "IDR ÷ 17500",
        "langkah": f"{idr} IDR menjadi €{round(hasil,2)}"
    }

def idr_ke_sgd(idr):

    rate = 12000

    hasil = idr / rate

    return {
        "hasil": round(hasil, 2),
        "rumus": "IDR ÷ 12000",
        "langkah": f"{idr} IDR menjadi SGD {round(hasil,2)}"
    }