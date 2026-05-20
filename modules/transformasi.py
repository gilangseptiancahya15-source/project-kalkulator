def konversi_bilangan(angka_str, dari, ke):
    try:
        # Convert to Decimal first
        if dari == "desimal":
            dec = int(angka_str)
        elif dari == "biner":
            dec = int(angka_str, 2)
        elif dari == "oktal":
            dec = int(angka_str, 8)
        elif dari == "heksa":
            dec = int(angka_str, 16)
        else:
            return {"hasil": "Error", "rumus": "-", "langkah": "Basis asal tidak valid"}
    except ValueError:
        return {"hasil": "Error", "rumus": "-", "langkah": f"Input '{angka_str}' tidak valid untuk bilangan {dari}"}

    # Convert from Decimal to Target
    if ke == "desimal":
        res = str(dec)
    elif ke == "biner":
        res = bin(dec)[2:]
    elif ke == "oktal":
        res = oct(dec)[2:]
    elif ke == "heksa":
        res = hex(dec)[2:].upper()
    else:
        return {"hasil": "Error", "rumus": "-", "langkah": "Basis tujuan tidak valid"}

    return {
        "hasil": res,
        "rumus": f"{dari.capitalize()} → {ke.capitalize()}",
        "langkah": f"{angka_str} ({dari.capitalize()}) dikonversi menjadi {res} ({ke.capitalize()})"
    }

def konversi_suhu(suhu, dari, ke):
    try:
        suhu = float(suhu)
    except ValueError:
        return {"hasil": "Error", "rumus": "-", "langkah": "Suhu harus berupa angka"}

    # Convert to Celcius first
    if dari == "celcius":
        c = suhu
    elif dari == "fahrenheit":
        c = (suhu - 32) * 5/9
    elif dari == "kelvin":
        c = suhu - 273.15
    elif dari == "reamur":
        c = suhu * 5/4
    else:
        return {"hasil": "Error", "rumus": "-", "langkah": "Basis asal tidak valid"}

    # Convert from Celcius to Target
    if ke == "celcius":
        res = c
    elif ke == "fahrenheit":
        res = (c * 9/5) + 32
    elif ke == "kelvin":
        res = c + 273.15
    elif ke == "reamur":
        res = c * 4/5
    else:
        return {"hasil": "Error"}

    return {
        "hasil": round(res, 2),
        "rumus": f"{dari.capitalize()} → {ke.capitalize()}",
        "langkah": f"{suhu} {dari.capitalize()} dikonversi menjadi {round(res, 2)} {ke.capitalize()}"
    }

def konversi_mata_uang(jumlah, dari, ke):
    try:
        jumlah = float(jumlah)
    except ValueError:
        return {"hasil": "Error", "rumus": "-", "langkah": "Jumlah harus berupa angka"}

    # rates relative to IDR (simple mock rates)
    rates = {
        "idr": 1,
        "usd": 16000,
        "eur": 17500,
        "sgd": 12000
    }
    
    if dari not in rates or ke not in rates:
        return {"hasil": "Error", "rumus": "-", "langkah": "Mata uang tidak didukung"}

    # Convert to IDR
    idr = jumlah * rates[dari]
    
    # Convert IDR to Target
    res = idr / rates[ke]
    
    return {
        "hasil": round(res, 2),
        "rumus": f"{dari.upper()} → {ke.upper()}",
        "langkah": f"{jumlah} {dari.upper()} dikonversi menjadi {round(res, 2)} {ke.upper()}"
    }