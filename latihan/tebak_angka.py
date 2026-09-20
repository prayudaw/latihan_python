import random

def main():
    print("=" * 45)
    print("    Selamat Datang di Game Tebak Angka!    ")
    print("=" * 45)
    
    while True:
        # Menghasilkan angka acak dari 1 sampai 100
        angka_rahasia = random.randint(1, 10)
        percobaan = 0
        
        print("\nSaya telah memikirkan sebuah angka antara 1 sampai 100.")
        print("Coba tebak angka berapakah itu!")
        
        while True:
            tebakan_str = input("\nMasukkan tebakan Anda: ")
            
            # Validasi input (memastikan input adalah angka)
            if not tebakan_str.isdigit():
                print("Error: Harap masukkan angka bulat yang valid!")
                continue
                
            tebakan = int(tebakan_str)
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Tebakan Anda terlalu kecil! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Tebakan Anda terlalu besar! Coba lagi.")
            else:
                print(f"\nSelamat! Tebakan Anda BENAR.")
                print(f"Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan!")
                break
                
        # Opsi untuk bermain lagi
        main_lagi = input("\nApakah Anda ingin bermain lagi? (y/n): ").strip().lower()
        if main_lagi != 'y':
            print("\nTerima kasih telah bermain! Sampai jumpa.")
            break

if __name__ == "__main__":
    main()
