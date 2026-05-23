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
    
    langkah = []
    if dari != "desimal":
        langkah.append(f"Ubah {dari.capitalize()} ke Desimal:")
        if dari == "biner":
            langkah.append(f"Biner {angka_str} -> Desimal = {dec}")
        elif dari == "oktal":
            langkah.append(f"Oktal {angka_str} -> Desimal = {dec}")
        elif dari == "heksa":
            langkah.append(f"Heksa {angka_str} -> Desimal = {dec}")
    
    if ke != "desimal":
        langkah.append(f"Ubah Desimal {dec} ke {ke.capitalize()}:")
        langkah.append(f"Desimal {dec} -> {ke.capitalize()} = {res}")
        
    if dari == ke:
        langkah.append("Tidak ada konversi yang diperlukan (basis asal dan tujuan sama).")


    return {
        "hasil": res,
        "rumus": f"{dari.capitalize()} → {ke.capitalize()}",
         "langkah": langkah
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
    
    langkah = []
    if dari != "celcius":
        langkah.append(f"1. Ubah {dari.capitalize()} ke Celcius:")
        if dari == "fahrenheit":
            langkah.append(f"&nbsp;&nbsp;&nbsp;C = ({suhu} - 32) * 5/9 = {c}")
        elif dari == "kelvin":
            langkah.append(f"&nbsp;&nbsp;&nbsp;C = {suhu} - 273.15 = {c}")
        elif dari == "reamur":
            langkah.append(f"&nbsp;&nbsp;&nbsp;C = {suhu} * 5/4 = {c}")
            
    if ke != "celcius":
        langkah.append(f"2. Ubah Celcius ({c}) ke {ke.capitalize()}:")
        if ke == "fahrenheit":
            langkah.append(f"&nbsp;&nbsp;&nbsp;F = ({c} * 9/5) + 32 = {res}")
        elif ke == "kelvin":
            langkah.append(f"&nbsp;&nbsp;&nbsp;K = {c} + 273.15 = {res}")
        elif ke == "reamur":
            langkah.append(f"&nbsp;&nbsp;&nbsp;R = {c} * 4/5 = {res}")
            
    if dari == ke:
        langkah.append("Tidak ada konversi (suhu asal dan tujuan sama).")


    return {
        "hasil": round(res, 2),
        "rumus": f"{dari.capitalize()} → {ke.capitalize()}",
        "langkah": langkah
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

    langkah = []
    if dari != "idr":
        langkah.append(f"1. Ubah {dari.upper()} ke IDR (Rate: {rates[dari]}):")
        langkah.append(f"&nbsp;&nbsp;&nbsp;{jumlah} * {rates[dari]} = {idr}")
    
    if ke != "idr":
        langkah.append(f"2. Ubah IDR ke {ke.upper()} (Rate: {rates[ke]}):")
        langkah.append(f"&nbsp;&nbsp;&nbsp;{idr} / {rates[ke]} = {round(res, 2)}")
        
    if dari == ke:
        langkah.append("Tidak ada konversi (mata uang asal dan tujuan sama).")
    
    return {
        "hasil": round(res, 2),
        "rumus": f"{dari.upper()} → {ke.upper()}",
        "langkah": langkah
    }