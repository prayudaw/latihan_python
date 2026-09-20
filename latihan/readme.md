# 🧮 Kalkulator Sederhana dengan Python

Panduan step-by-step membuat aplikasi kalkulator sederhana menggunakan Python.

---

## 📋 Deskripsi

Aplikasi kalkulator ini dapat melakukan 4 operasi dasar matematika:
- **Penjumlahan** (+)
- **Pengurangan** (-)
- **Perkalian** (×)
- **Pembagian** (÷)

---

## 🚀 Step-by-Step Pembuatan

### Step 1: Membuat Fungsi Operasi Matematika

Buat 4 fungsi untuk masing-masing operasi:

```python
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b
```

**Penjelasan:**
- Setiap fungsi menerima 2 parameter (`a` dan `b`)
- Fungsi `bagi` memiliki pengecekan khusus: jika `b = 0`, maka akan menampilkan pesan error karena pembagian dengan nol tidak diperbolehkan

---

### Step 2: Menampilkan Menu Pilihan Operasi

Buat fungsi untuk menampilkan menu ke pengguna:

```python
def tampilkan_menu():
    print("\n============================")
    print("   KALKULATOR SEDERHANA")
    print("============================")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (x)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    print("============================")
```

**Penjelasan:**
- Fungsi `print()` digunakan untuk menampilkan teks ke layar
- `\n` di awal berfungsi menambah baris kosong agar tampilan lebih rapi

---

### Step 3: Meminta Input dari Pengguna

Minta pengguna memilih operasi dan memasukkan angka:

```python
pilihan = input("Pilih operasi (1-5): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
```

**Penjelasan:**
- `input()` digunakan untuk meminta masukan dari pengguna melalui keyboard
- `float()` mengubah teks input menjadi angka desimal agar bisa dihitung

---

### Step 4: Memproses Pilihan dengan Kondisi `if-elif-else`

Jalankan operasi sesuai pilihan pengguna:

```python
if pilihan == "1":
    hasil = tambah(angka1, angka2)
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif pilihan == "2":
    hasil = kurang(angka1, angka2)
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif pilihan == "3":
    hasil = kali(angka1, angka2)
    print(f"Hasil: {angka1} x {angka2} = {hasil}")
elif pilihan == "4":
    hasil = bagi(angka1, angka2)
    print(f"Hasil: {angka1} / {angka2} = {hasil}")
```

**Penjelasan:**
- `if-elif-else` digunakan untuk memeriksa pilihan pengguna
- `f"..."` adalah **f-string**, cara modern di Python untuk menyisipkan variabel ke dalam teks

---

### Step 5: Membuat Loop agar Program Berjalan Berulang

Bungkus semuanya dalam `while True` agar kalkulator bisa dipakai berulang kali:

```python
while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (1-5): ")

    if pilihan == "5":
        print("Terima kasih! Sampai jumpa 👋")
        break

    # minta input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # proses sesuai pilihan
    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == "2":
        # ... dan seterusnya
```

**Penjelasan:**
- `while True` membuat loop tak terbatas — program terus berjalan sampai pengguna memilih "Keluar"
- `break` digunakan untuk menghentikan loop dan keluar dari program

---

### Step 6: Menambahkan Error Handling

Tambahkan `try-except` untuk menangani input yang salah:

```python
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("❌ Input tidak valid! Masukkan angka yang benar.")
    continue
```

**Penjelasan:**
- `try-except` menangkap error jika pengguna memasukkan huruf/teks bukan angka
- `continue` melompat kembali ke awal loop untuk mengulangi input

---

## 📄 Kode Lengkap

Lihat file **[kalkulator.py](./kalkulator.py)** untuk kode lengkap yang siap dijalankan.

---

## ▶️ Cara Menjalankan

```bash
cd d:\python\latihan1
python kalkulator.py
```

---

## 📸 Contoh Output

```
============================
   KALKULATOR SEDERHANA
============================
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (x)
4. Pembagian (/)
5. Keluar
============================
Pilih operasi (1-5): 1
Masukkan angka pertama: 10
Masukkan angka kedua: 5
Hasil: 10.0 + 5.0 = 15.0
```

---

## 📚 Konsep Python yang Dipelajari

| No | Konsep | Keterangan |
|----|--------|------------|
| 1 | `def` (fungsi) | Membuat blok kode yang bisa dipanggil ulang |
| 2 | `input()` | Meminta masukan dari pengguna |
| 3 | `float()` | Mengubah teks menjadi angka desimal |
| 4 | `if-elif-else` | Percabangan / kondisi logika |
| 5 | `while` loop | Pengulangan sampai kondisi tertentu |
| 6 | `try-except` | Penanganan error (error handling) |
| 7 | f-string | Format string modern Python |
| 8 | `break` / `continue` | Kontrol alur loop |
