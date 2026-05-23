import math

def tambah(a, b):
    hasil = a + b

    return {
        "hasil": hasil,
        "rumus": f"{a} + {b}",
        "langkah": [
            "1. Identifikasi Operasi: Penjumlahan (+)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} + {b} = {hasil}"
        ]
    }

def kurang(a, b):
    hasil = a - b

    return {
        "hasil": hasil,
        "rumus": f"{a} - {b}",
        "langkah": [
            "1. Identifikasi Operasi: Pengurangan (-)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} - {b} = {hasil}"
        ]
    }

def kali(a, b):
    hasil = a * b

    return {
        "hasil": hasil,
        "rumus": f"{a} × {b}",
         "langkah": [
            "1. Identifikasi Operasi: Perkalian (×)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} × {b} = {hasil}"
        ]
    }

def bagi(a, b):

    if b == 0:
        return {
            "hasil": "Error",
            "rumus": "Pembagian",
            "langkah": "Tidak bisa dibagi dengan 0"
        }

    hasil = a / b

    return {
        "hasil": hasil,
        "rumus": f"{a} ÷ {b}",
        "langkah": [
            "1. Identifikasi Operasi: Pembagian (÷)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} ÷ {b} = {hasil}"
        ]
    }

def modulus(a, b):
    hasil = a % b

    return {
        "hasil": hasil,
        "rumus": f"{a} % {b}",
          "langkah": [
            "1. Identifikasi Operasi: Modulus / Sisa Bagi (%)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} % {b} = {hasil}"
        ]
    }

def pangkat(a, b):
    hasil = a ** b

    return {
        "hasil": hasil,
        "rumus": f"{a}^{b}",
        "langkah": [
            "1. Identifikasi Operasi: Pemangkatan (^)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a}^{b} = {hasil}"
        ]
    }

def akar(a):
    hasil = math.sqrt(a)

    return {
        "hasil": hasil,
        "rumus": f"√{a}",
         "langkah": [
            "1. Identifikasi Operasi: Akar Kuadrat (√)",
            f"2. Nilai = {a}",
            f"3. Hitung: √{a} = {hasil}"
        ]
    }

def floor_division(a, b):
    hasil = a // b

    return {
        "hasil": hasil,
        "rumus": f"{a} // {b}",
        "langkah": [
            "1. Identifikasi Operasi: Pembagian Floor (//)",
            f"2. Nilai a = {a}, Nilai b = {b}",
            f"3. Hitung: {a} // {b} = {hasil}"
        ]
    }

def faktorial(a):
    hasil = math.factorial(int(a))

    langkah = [
        "1. Identifikasi Operasi: Faktorial (!)",
        f"2. Nilai = {a}"
    ]
    if int(a) <= 10:
        deret = " × ".join(str(i) for i in range(int(a), 0, -1))
        langkah.append(f"3. Penjabaran: {deret}")
    langkah.append(f"Hasil: {a}! = {hasil}")

    return {
        "hasil": hasil,
        "rumus": f"{a}!",
        "langkah": langkah
    }

def fibonacci(n):

    deret = [0, 1]

    for i in range(2, int(n)):
        deret.append(deret[i - 1] + deret[i - 2])

    return {
        "hasil": deret,
        "rumus": "Fibonacci",
        "langkah": [
            "1. Identifikasi Operasi: Deret Fibonacci",
            f"2. Jumlah angka = {n}",
            f"3. Deret: {', '.join(map(str, deret))}"
        ]
    }