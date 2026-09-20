def tampilkan_menu():
    print("=" * 45)
    print("      Aplikasi Konversi Suhu      ")
    print("=" * 45)
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")
    print("4. Kelvin ke Celsius")
    print("5. Keluar")
    print("=" * 45)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu konversi (1-5): ")

        if pilihan == '5':
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            break

        if pilihan in ['1', '2', '3', '4']:
            # Menerima input suhu dan validasi
            try:
                suhu_input = input("\nMasukkan nilai suhu: ")
                suhu = float(suhu_input)
            except ValueError:
                print("\nError: Harap masukkan angka yang valid!")
                input("Tekan Enter untuk melanjutkan...")
                continue

            # Melakukan perhitungan sesuai pilihan
            if pilihan == '1':
                hasil = (suhu * 9/5) + 32
                print(f"\n✅ {suhu}°C = {hasil:.2f}°F")
            elif pilihan == '2':
                hasil = (suhu - 32) * 5/9
                print(f"\n✅ {suhu}°F = {hasil:.2f}°C")
            elif pilihan == '3':
                hasil = suhu + 273.15
                print(f"\n✅ {suhu}°C = {hasil:.2f}K")
            elif pilihan == '4':
                hasil = suhu - 273.15
                print(f"\n✅ {suhu}K = {hasil:.2f}°C")
                
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
