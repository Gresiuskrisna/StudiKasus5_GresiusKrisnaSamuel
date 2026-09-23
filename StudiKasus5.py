# menghitung biaya parkir
def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan.lower() == "mobil":
        tarif = 5000
    elif jenis_kendaraan.lower() == "motor":
        tarif = 3000
    else:
        tarif = 0

    total_biaya = tarif * durasi_parkir
    return total_biaya


# input data
def hitung_parkir():
    print("======= Input Data Parkir =======")
    jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil/Motor): ")
    jam_masuk = int(input("Masukkan jam masuk: "))
    jam_keluar = int(input("Masukkan jam keluar: "))

    # Menghitung lama parkir
    lama_parkir = jam_keluar - jam_masuk

    # Memanggil function hitung_biaya_parkir
    total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

    # Output
    print("\n======= Biaya Parkir =======")
    print("Jenis Kendaraan   :", jenis_kendaraan)
    print("Jam Masuk         :", jam_masuk)
    print("Jam Keluar        :", jam_keluar)
    print("Lama Parkir       :", lama_parkir, "jam")
    print("Total Biaya Parkir: Rp", total_biaya)


# Menu
while True:
    print("\n======= Menu Parkir =======")
    print("1. Hitung Biaya Parkir")
    print("2. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        hitung_parkir()
    elif pilihan == "2":
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid")