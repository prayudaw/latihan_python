def tampilkan_menu():
    print("\n" + "=" * 35)
    print("      Aplikasi To-Do List CLI      ")
    print("=" * 35)
    print("1. Lihat Daftar Tugas (Read)")
    print("2. Tambah Tugas Baru (Create)")
    print("3. Ubah Tugas (Update)")
    print("4. Hapus Tugas (Delete)")
    print("5. Keluar")
    print("=" * 35)

def main():
    # List kosong untuk menyimpan tugas secara sementara di memori
    todos = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            # READ: Menampilkan seluruh tugas
            print("\n--- Daftar Tugas Anda ---")
            if not todos:
                print("Belum ada tugas dalam daftar.")
            else:
                for idx, tugas in enumerate(todos, start=1):
                    print(f"{idx}. {tugas}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '2':
            # CREATE: Menambah tugas baru ke dalam list
            tugas_baru = input("\nMasukkan tugas baru: ").strip()
            if tugas_baru:
                todos.append(tugas_baru)
                print(f"✅ Tugas '{tugas_baru}' berhasil ditambahkan!")
            else:
                print("⚠️ Error: Tugas tidak boleh kosong!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '3':
            # UPDATE: Mengubah tugas berdasarkan nomor urut (indeks)
            if not todos:
                print("\n⚠️ Belum ada tugas yang bisa diubah.")
                input("\nTekan Enter untuk kembali ke menu...")
                continue
                
            print("\n--- Daftar Tugas Anda ---")
            for idx, tugas in enumerate(todos, start=1):
                print(f"{idx}. {tugas}")
                
            try:
                nomor = int(input("\nMasukkan nomor tugas yang ingin diubah: "))
                # Validasi nomor apakah ada di dalam range list
                if 1 <= nomor <= len(todos):
                    tugas_lama = todos[nomor - 1]
                    tugas_baru = input(f"Masukkan tugas pengganti untuk '{tugas_lama}': ").strip()
                    if tugas_baru:
                        todos[nomor - 1] = tugas_baru
                        print(f"✅ Tugas '{tugas_lama}' berhasil diubah menjadi '{tugas_baru}'!")
                    else:
                        print("⚠️ Error: Tugas tidak boleh kosong!")
                else:
                    print("⚠️ Error: Nomor tugas tidak ditemukan!")
            except ValueError:
                print("⚠️ Error: Harap masukkan angka yang valid!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '4':
            # DELETE: Menghapus tugas berdasarkan nomor urut (indeks)
            if not todos:
                print("\n⚠️ Belum ada tugas yang bisa dihapus.")
                input("\nTekan Enter untuk kembali ke menu...")
                continue
                
            print("\n--- Daftar Tugas Anda ---")
            for idx, tugas in enumerate(todos, start=1):
                print(f"{idx}. {tugas}")
                
            try:
                nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                # Validasi nomor apakah ada di dalam range list
                if 1 <= nomor <= len(todos):
                    tugas_hapus = todos.pop(nomor - 1)
                    print(f"✅ Tugas '{tugas_hapus}' berhasil dihapus!")
                else:
                    print("⚠️ Error: Nomor tugas tidak ditemukan!")
            except ValueError:
                print("⚠️ Error: Harap masukkan angka yang valid!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan Aplikasi To-Do List! Sampai jumpa.")
            break
        else:
            print("\n⚠️ Pilihan tidak valid, silakan coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
