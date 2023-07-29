# Inisialisasi variabel stok
stok_barang = {
    "beras": {"jumlah": 50, "harga": 10000},
    "gula": {"jumlah": 30, "harga": 8000},
    "minyak": {"jumlah": 40, "harga": 15000},
    "telur": {"jumlah": 60, "harga": 2500},
    "tepung": {"jumlah": 20, "harga": 5000}
}

# Fungsi untuk menampilkan stok barang
def tampilkan_stok():
    print("Stok Barang:")
    print("===================================")
    print("|    Barang    |  Jumlah  |   Harga  |")
    print("===================================")
    for barang, data in stok_barang.items():
        print("|%-13s|%10d|%10d|" % (barang.capitalize(), data["jumlah"], data["harga"]))
    print("===================================")

# Fungsi untuk membeli barang
def beli_barang(barang, jumlah):
    if barang in stok_barang:
        if jumlah <= stok_barang[barang]["jumlah"]:
            total_harga = stok_barang[barang]["harga"] * jumlah
            stok_barang[barang]["jumlah"] -= jumlah
            print("Anda telah membeli %d %s dengan total harga Rp%d." % (jumlah, barang, total_harga))
        else:
            print("Maaf, stok %s tidak mencukupi." % barang)
    else:
        print("Maaf, barang yang Anda masukkan tidak tersedia.")

# Looping program utama
while True:
    print("\nSelamat datang di Toko Sembako!")
    print("1. Tampilkan stok barang")
    print("2. Beli barang")
    print("3. Tambah stok barang")
    print("4. Keluar")
    pilihan = input("Silakan pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tampilkan_stok()
    elif pilihan == "2":
        barang = input("Masukkan barang yang ingin dibeli: ")
        jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        beli_barang(barang, jumlah)
    elif pilihan == "3":
        barang = input("Masukkan barang yang ingin ditambahkan stoknya: ")
        jumlah = int(input("Masukkan jumlah barang yang ingin ditambahkan: "))

        if barang in stok_barang:
            stok_barang[barang]["jumlah"] += jumlah
            print("Stok %s berhasil ditambahkan sebanyak %d." % (barang, jumlah))
        else:
            harga = int(input("Masukkan harga barang: "))
            stok_barang[barang] = {"jumlah": jumlah, "harga": harga}
            print("Stok %s berhasil ditambahkan sebanyak %d dengan harga Rp%d." % (barang, jumlah, harga))
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa lagi!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
