def operasi_and(a, b):
    hasil = a and b
    return {
        "hasil": hasil,
        "rumus": f"{a} AND {b}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika AND",
            f"2. Input A = {a}, Input B = {b}",
            f"3. Syarat AND: Bernilai True jika keduanya True",
            f"4. Hasil Akhir = {hasil}"
        ]
    }

def operasi_or(a, b):
    hasil = a or b
    return {
        "hasil": hasil,
        "rumus": f"{a} OR {b}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika OR",
            f"2. Input A = {a}, Input B = {b}",
            f"3. Syarat OR: Bernilai True jika minimal satu dari keduanya True",
            f"4. Hasil Akhir = {hasil}"
        ]
    }

def operasi_not(a):
    hasil = not a
    return {
        "hasil": hasil,
        "rumus": f"NOT {a}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika NOT",
            f"2. Input = {a}",
            f"3. Syarat NOT: Bernilai True jika input False",
            f"4. Hasil Akhir = {hasil}"
        ]
    }

def operasi_xor(a, b):
    hasil = bool(a) ^ bool(b)
    return {
        "hasil": hasil,
        "rumus": f"{a} XOR {b}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika XOR",
            f"2. Input A = {a}, Input B = {b}",
            f"3. Syarat XOR: Bernilai True jika hanya satu dari keduanya True",
            f"4. Hasil Akhir = {hasil}"
        ]
    }

def operasi_nand(a, b):
    hasil = not (a and b)
    return {
        "hasil": hasil,
        "rumus": f"{a} NAND {b}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika NAND",
            f"2. Input A = {a}, Input B = {b}",
            f"3. Syarat NAND: Bernilai True jika keduanya False",
            f"4. Hasil Akhir = {hasil}"
        ]
    }

def operasi_nor(a, b):
    hasil = not (a or b)
    return {
        "hasil": hasil,
        "rumus": f"{a} NOR {b}",
        "langkah": [
            "1. Identifikasi Operasi: Gerbang Logika NOR",
            f"2. Input A = {a}, Input B = {b}",
            f"3. Syarat NOR: Bernilai True jika keduanya False",
            f"4. Hasil Akhir = {hasil}"
        ]
    }