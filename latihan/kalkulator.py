# ============================
# Kalkulator Sederhana Python
# ============================

# Step 1: Membuat fungsi operasi matematika

def tambah(a, b):
    """Menjumlahkan dua angka."""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka."""
    return a - b

def kali(a, b):
    """Mengalikan dua angka."""
    return a * b

def bagi(a, b):
    """Membagi dua angka dengan pengecekan pembagi nol."""
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b


# Step 2: Membuat fungsi tampilkan menu

def tampilkan_menu():
    """Menampilkan menu pilihan operasi."""
    print("\n============================")
    print("   KALKULATOR SEDERHANA")
    print("============================")
    print("1. Penjumlahan  (+)")
    print("2. Pengurangan  (-)")
    print("3. Perkalian    (x)")
    print("4. Pembagian    (/)")
    print("5. Keluar")
    print("============================")


# Step 3-6: Program utama dengan loop, input, kondisi, dan error handling

def main():
    """Fungsi utama yang menjalankan kalkulator."""
    while True:
        # Tampilkan menu
        tampilkan_menu()

        # Minta pilihan operasi
        pilihan = input("Pilih operasi (1-5): ")

        # Cek jika pengguna ingin keluar
        if pilihan == "5":
            print("\nTerima kasih! Sampai jumpa 👋")
            break

        # Validasi pilihan
        if pilihan not in ("1", "2", "3", "4"):
            print("❌ Pilihan tidak valid! Silakan pilih 1-5.")
            continue

        # Minta input angka dengan error handling
        try:
            angka1 = float(input("Masukkan angka pertama : "))
            angka2 = float(input("Masukkan angka kedua   : "))
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka yang benar.")
            continue

        # Proses sesuai pilihan
        if pilihan == "1":
            hasil = tambah(angka1, angka2)
            print(f"\n✅ Hasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == "2":
            hasil = kurang(angka1, angka2)
            print(f"\n✅ Hasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == "3":
            hasil = kali(angka1, angka2)
            print(f"\n✅ Hasil: {angka1} x {angka2} = {hasil}")
        elif pilihan == "4":
            hasil = bagi(angka1, angka2)
            print(f"\n✅ Hasil: {angka1} / {angka2} = {hasil}")


# Jalankan program
if __name__ == "__main__":
    main()
