# Studi Kasus 5 Perhitungan Biaya Parkir

Nama: Gresius Krisna Samuel
NIM: 058
Kelas: B


# Penjelasan Kode Program

# Fungsi hitung_biaya_parkir
Baris 1-8: Fungsi hitung_biaya_parkir menerima parameter jenis_kendaraan dan durasi_parkir. Percabangan di dalamnya dipakai buat menentukan tarif parkir, yaitu mobil 5000 dan motor 3000. Penggunaan lower bertujuan supaya input huruf besar atau kecil tetap terbaca sama

Baris 10-11: Menghitung total_biaya dari tarif dikali durasi_parkir, lalu mengembalikan nilainya memakai return

# Fungsi hitung_parkir
Baris 15-19: Fungsi hitung_parkir dipakai buat mengambil input jenis kendaraan, jam masuk, dan jam keluar. Fungsi int dipakai untuk mengubah input teks menjadi integer supaya bisa dihitung

Baris 21-25: Menghitung lama_parkir dari selisih jam masuk dan jam keluar. Selanjutnya memanggil fungsi hitung_biaya_parkir dan menyimpan hasilnya di variabel total_biaya

Baris 27-33: Menampilkan hasil perhitungan parkir, seperti jenis kendaraan, jam masuk, jam keluar, lama parkir, dan total biaya


# Perulangan Menu Utama
Baris 37-42: Memakai perulangan while True supaya menu program terus berjalan sampai pengguna memilih keluar

Baris 44-50: Percabangan buat mengatur pilihan menu. Pilihan 1 memanggil fungsi hitung_parkir, pilihan 2 menghentikan program dengan break, dan input selain itu akan menampilkan pesan pilihan tidak valid.


# Output Program
<img width="720" height="932" alt="17856" src="https://github.com/user-attachments/assets/7d0f3eb1-399b-4cd7-b0d9-1e9d956449b8" />
