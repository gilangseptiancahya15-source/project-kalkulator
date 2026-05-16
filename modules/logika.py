def operasi_and(a, b):
    hasil = a and b
    return {
        "hasil": hasil,
        "rumus": f"{a} AND {b}",
        "langkah": f"Hasil AND = {hasil}"
    }

def operasi_or(a, b):
    hasil = a or b
    return {
        "hasil": hasil,
        "rumus": f"{a} OR {b}",
        "langkah": f"Hasil OR = {hasil}"
    }

def operasi_not(a):
    hasil = not a
    return {
        "hasil": hasil,
        "rumus": f"NOT {a}",
        "langkah": f"Hasil NOT = {hasil}"
    }

def operasi_xor(a, b):
    hasil = bool(a) ^ bool(b)
    return {
        "hasil": hasil,
        "rumus": f"{a} XOR {b}",
        "langkah": f"Hasil XOR = {hasil}"
    }

def operasi_nand(a, b):
    hasil = not (a and b)
    return {
        "hasil": hasil,
        "rumus": f"{a} NAND {b}",
        "langkah": f"Hasil NAND = {hasil}"
    }

def operasi_nor(a, b):
    hasil = not (a or b)
    return {
        "hasil": hasil,
        "rumus": f"{a} NOR {b}",
        "langkah": f"Hasil NOR = {hasil}"
    }