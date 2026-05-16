import math

def tambah(a, b):
    hasil = a + b

    return {
        "hasil": hasil,
        "rumus": f"{a} + {b}",
        "langkah": f"{a} ditambah {b} = {hasil}"
    }

def kurang(a, b):
    hasil = a - b

    return {
        "hasil": hasil,
        "rumus": f"{a} - {b}",
        "langkah": f"{a} dikurang {b} = {hasil}"
    }

def kali(a, b):
    hasil = a * b

    return {
        "hasil": hasil,
        "rumus": f"{a} × {b}",
        "langkah": f"{a} dikali {b} = {hasil}"
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
        "langkah": f"{a} dibagi {b} = {hasil}"
    }

def modulus(a, b):
    hasil = a % b

    return {
        "hasil": hasil,
        "rumus": f"{a} % {b}",
        "langkah": f"Sisa hasil bagi {a} % {b} = {hasil}"
    }

def pangkat(a, b):
    hasil = a ** b

    return {
        "hasil": hasil,
        "rumus": f"{a}^{b}",
        "langkah": f"{a} pangkat {b} = {hasil}"
    }

def akar(a):
    hasil = math.sqrt(a)

    return {
        "hasil": hasil,
        "rumus": f"√{a}",
        "langkah": f"Akar dari {a} = {hasil}"
    }

def floor_division(a, b):
    hasil = a // b

    return {
        "hasil": hasil,
        "rumus": f"{a} // {b}",
        "langkah": f"Floor division {a} // {b} = {hasil}"
    }

def faktorial(a):
    hasil = math.factorial(int(a))

    return {
        "hasil": hasil,
        "rumus": f"{a}!",
        "langkah": f"Faktorial dari {a} = {hasil}"
    }

def fibonacci(n):

    deret = [0, 1]

    for i in range(2, int(n)):
        deret.append(deret[i - 1] + deret[i - 2])

    return {
        "hasil": deret,
        "rumus": "Fibonacci",
        "langkah": f"Deret fibonacci {n} angka pertama"
    }