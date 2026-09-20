<?php
// ============================
// Kalkulator Sederhana PHP
// ============================

// Step 1: Membuat fungsi operasi matematika

function tambah($a, $b) {
    return $a + $b;
}

function kurang($a, $b) {
    return $a - $b;
}

function kali($a, $b) {
    return $a * $b;
}

function bagi($a, $b) {
    if ($b == 0) {
        return "Error: Tidak bisa membagi dengan nol!";
    }
    return $a / $b;
}


// Step 2: Membuat fungsi tampilkan menu

function tampilkan_menu() {
    echo "\n============================\n";
    echo "   KALKULATOR SEDERHANA\n";
    echo "============================\n";
    echo "1. Penjumlahan  (+)\n";
    echo "2. Pengurangan  (-)\n";
    echo "3. Perkalian    (x)\n";
    echo "4. Pembagian    (/)\n";
    echo "5. Keluar\n";
    echo "============================\n";
}


// Step 3-6: Program utama dengan loop, input, kondisi, dan error handling

while (true) {
    // Tampilkan menu
    tampilkan_menu();

    // Minta pilihan operasi
    $pilihan = trim(readline("Pilih operasi (1-5): "));

    // Cek jika pengguna ingin keluar
    if ($pilihan == "5") {
        echo "\nTerima kasih! Sampai jumpa 👋\n";
        break;
    }

    // Validasi pilihan
    if (!in_array($pilihan, ["1", "2", "3", "4"])) {
        echo "❌ Pilihan tidak valid! Silakan pilih 1-5.\n";
        continue;
    }

    // Minta input angka
    $angka1 = (float) readline("Masukkan angka pertama : ");
    $angka2 = (float) readline("Masukkan angka kedua   : ");

    // Proses sesuai pilihan
    if ($pilihan == "1") {
        $hasil = tambah($angka1, $angka2);
        echo "\n✅ Hasil: $angka1 + $angka2 = $hasil\n";
    } elseif ($pilihan == "2") {
        $hasil = kurang($angka1, $angka2);
        echo "\n✅ Hasil: $angka1 - $angka2 = $hasil\n";
    } elseif ($pilihan == "3") {
        $hasil = kali($angka1, $angka2);
        echo "\n✅ Hasil: $angka1 x $angka2 = $hasil\n";
    } elseif ($pilihan == "4") {
        $hasil = bagi($angka1, $angka2);
        echo "\n✅ Hasil: $angka1 / $angka2 = $hasil\n";
    }
}
?>
