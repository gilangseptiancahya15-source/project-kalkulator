# 🧮 KalkulatorKu

**KalkulatorKu** adalah aplikasi kalkulator berbasis web yang dibangun menggunakan Python Flask. Aplikasi ini mendukung tiga kategori operasi utama: **Aritmatika**, **Logika**, dan **Transformasi**, lengkap dengan penjelasan langkah-langkah penyelesaian untuk setiap perhitungan.

> Tugas Mata Kuliah **Pengantar Pemrograman** — Semester 2

---

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Struktur Proyek](#-struktur-proyek)
- [Prasyarat](#-prasyarat)
- [Instalasi & Menjalankan](#-instalasi--menjalankan)
- [Panduan Penggunaan](#-panduan-penggunaan)
- [Penjelasan Modul](#-penjelasan-modul)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)

---

## ✨ Fitur

### 1. Aritmatika
| Operasi | Simbol | Keterangan |
|---------|--------|------------|
| Penjumlahan | `+` | Menjumlahkan dua angka |
| Pengurangan | `−` | Mengurangkan dua angka |
| Perkalian | `×` | Mengalikan dua angka |
| Pembagian | `÷` | Membagi dua angka (dengan validasi pembagian nol) |
| Modulus | `%` | Menghitung sisa bagi |
| Pangkat | `^` | Menghitung perpangkatan |
| Akar Kuadrat | `√` | Menghitung akar kuadrat (hanya input pertama) |
| Pembagian Bulat | `//` | Menghitung pembagian bulat (floor division) |
| Faktorial | `!` | Menghitung faktorial dengan penjabaran langkah |
| Fibonacci | `Fib` | Menghasilkan deret Fibonacci sejumlah n elemen |

### 2. Gerbang Logika
| Operasi | Keterangan |
|---------|------------|
| AND | Bernilai `True` jika kedua input `True` |
| OR | Bernilai `True` jika salah satu input `True` |
| NOT | Membalik nilai input (hanya input pertama) |
| XOR | Bernilai `True` hanya jika input berbeda |
| NAND | Kebalikan dari hasil AND |
| NOR | Kebalikan dari hasil OR |

> **Catatan:** Input untuk operasi logika hanya menerima nilai `0` atau `1`.

### 3. Transformasi / Konversi
| Kategori | Konversi yang Tersedia |
|----------|----------------------|
| **Bilangan** | Desimal ↔ Biner ↔ Oktal ↔ Heksadesimal |
| **Suhu** | Celcius ↔ Fahrenheit ↔ Kelvin ↔ Reamur |
| **Mata Uang** | IDR ↔ USD ↔ EUR ↔ SGD |

### 4. Fitur Tambahan
- 📝 **Riwayat Perhitungan** — Menyimpan semua hasil perhitungan selama sesi berjalan
- 🗑️ **Hapus Riwayat** — Menghapus satu item atau seluruh riwayat sekaligus
- 🌗 **Dark/Light Mode** — Toggle tema gelap dan terang
- 📖 **Langkah Penyelesaian** — Setiap hasil dilengkapi rumus dan langkah-langkah perhitungan
- 📱 **Responsive Design** — Tampilan menyesuaikan ukuran layar (desktop & mobile)

---

## 📁 Struktur Proyek

```
Tugas kalkulator/
│
├── app.py                  # Entry point aplikasi Flask
├── requirements.txt        # Daftar dependensi Python
├── .gitignore              # File yang diabaikan Git
├── README.md               # Dokumentasi proyek (file ini)
│
├── modules/                # Modul-modul perhitungan
│   ├── aritmatika.py       # Fungsi operasi aritmatika
│   ├── logika.py           # Fungsi gerbang logika
│   └── transformasi.py     # Fungsi konversi/transformasi
│
├── templates/              # Template HTML (Jinja2)
│   └── index.html          # Halaman utama kalkulator
│
└── static/                 # File statis (CSS & JS)
    ├── css/
    │   └── style.css       # Stylesheet utama
    └── js/
        ├── script.js       # Logika interaksi UI
        └── darkmode.js     # Toggle dark/light mode
```

---

## 📦 Prasyarat

Pastikan perangkat lunak berikut sudah terinstal:

- **Python** 3.8 atau lebih baru — [Download Python](https://www.python.org/downloads/)
- **pip** (biasanya sudah termasuk dalam instalasi Python)
- **Git** (opsional, untuk clone repository)

---

## 🚀 Instalasi & Menjalankan

### 1. Clone atau Download Repository

```bash
git clone <url-repository>
cd "Tugas kalkulator"
```

### 2. Buat Virtual Environment (Disarankan)

```bash
# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Buka di Browser

Akses aplikasi melalui:

```
http://127.0.0.1:5000
```

---

## 📖 Panduan Penggunaan

1. **Pilih Kategori Operasi** — Klik tab **Aritmatika**, **Logika**, atau **Transformasi** pada navbar.
2. **Masukkan Angka** — Isi input angka pertama (dan angka kedua jika diperlukan).
3. **Pilih Operasi** — Klik tombol operasi yang diinginkan. Operasi yang dipilih akan ditampilkan di bawah tombol.
4. **Klik "Hitung"** — Tekan tombol hijau **Hitung** untuk memproses perhitungan.
5. **Lihat Hasil** — Hasil akan muncul beserta rumus dan langkah-langkah penyelesaiannya.
6. **Riwayat** — Semua hasil perhitungan otomatis tersimpan di bagian **Riwayat Perhitungan** di bawah.

### Khusus Transformasi:
- Pilih **sub-kategori** (Bilangan / Suhu / Mata Uang).
- Pilih satuan **asal** dan **tujuan** menggunakan dropdown.
- Masukkan nilai pada input angka pertama, lalu klik **Hitung**.

---

## 🔧 Penjelasan Modul

### `modules/aritmatika.py`
Berisi fungsi-fungsi operasi matematika dasar hingga lanjutan. Setiap fungsi mengembalikan dictionary berisi:
- `hasil` — Nilai hasil perhitungan
- `rumus` — Representasi rumus yang digunakan
- `langkah` — Daftar langkah-langkah penyelesaian

**Fungsi yang tersedia:**
| Fungsi | Parameter | Deskripsi |
|--------|-----------|-----------|
| `tambah(a, b)` | 2 angka | Penjumlahan |
| `kurang(a, b)` | 2 angka | Pengurangan |
| `kali(a, b)` | 2 angka | Perkalian |
| `bagi(a, b)` | 2 angka | Pembagian (validasi b ≠ 0) |
| `modulus(a, b)` | 2 angka | Sisa bagi |
| `pangkat(a, b)` | 2 angka | Perpangkatan |
| `akar(a)` | 1 angka | Akar kuadrat |
| `floor_division(a, b)` | 2 angka | Pembagian bulat |
| `faktorial(a)` | 1 angka | Faktorial (n!) |
| `fibonacci(n)` | 1 angka | Deret Fibonacci sejumlah n |

### `modules/logika.py`
Berisi fungsi-fungsi gerbang logika digital. Input berupa boolean (`True`/`False`).

**Fungsi yang tersedia:**
| Fungsi | Parameter | Deskripsi |
|--------|-----------|-----------|
| `operasi_and(a, b)` | 2 boolean | Gerbang AND |
| `operasi_or(a, b)` | 2 boolean | Gerbang OR |
| `operasi_not(a)` | 1 boolean | Gerbang NOT |
| `operasi_xor(a, b)` | 2 boolean | Gerbang XOR |
| `operasi_nand(a, b)` | 2 boolean | Gerbang NAND |
| `operasi_nor(a, b)` | 2 boolean | Gerbang NOR |

### `modules/transformasi.py`
Berisi fungsi-fungsi konversi antar satuan. Menggunakan pola konversi dua tahap (ke satuan dasar terlebih dahulu, lalu ke satuan tujuan).

**Fungsi yang tersedia:**
| Fungsi | Satuan Dasar | Satuan yang Didukung |
|--------|-------------|---------------------|
| `konversi_bilangan(angka_str, dari, ke)` | Desimal | Desimal, Biner, Oktal, Heksadesimal |
| `konversi_suhu(suhu, dari, ke)` | Celcius | Celcius, Fahrenheit, Kelvin, Reamur |
| `konversi_mata_uang(jumlah, dari, ke)` | IDR | IDR, USD, EUR, SGD |

> **Catatan:** Kurs mata uang menggunakan nilai statis (mock rates) untuk keperluan demonstrasi.

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|-----------|----------|
| **Python 3** | Bahasa pemrograman utama (back-end) |
| **Flask** | Web framework untuk routing dan templating |
| **Jinja2** | Template engine (terintegrasi dengan Flask) |
| **HTML5** | Struktur halaman web |
| **CSS3** | Styling dan responsive design |
| **JavaScript** | Interaksi UI dan dark mode |
| **Google Fonts (Poppins)** | Tipografi modern |
| **Git** | Version control |

---

## 👤 Informasi Pengembang

- **NIM:** 301250022
- **Mata Kuliah:** Pengantar Pemrograman
- **Semester:** 2

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan tugas akademik.

---

<p align="center">
  Dibuat dengan ❤️ menggunakan Python & Flask
</p>
