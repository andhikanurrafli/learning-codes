# Mengimpor pretty table
from prettytable import PrettyTable

# Membuat tabel
daftarMenu = PrettyTable()

# Menambahkan kolom
daftarMenu.add_column("Index", [0,1,2])
daftarMenu.add_column("Kopi", ["Americano", "Espresso", "Vietnam Drip"])
daftarMenu.add_column("Stok", [25, 30, 35])
daftarMenu.add_column("Harga", [15000, 10000, 13000])

# Membuat tampilan
print("Selamat datang di Warung Kopi Uhuy")

print("Daftar menu program: ")


while True:
    listMenu = ["1. Menampilkan Menu Kopi", "2. Menambah Menu Kopi", "3. Menghapus Menu Kopi",
                "4. Membeli Kopi", "5. Keluar Program"]
    for n in listMenu:
        print(n)
    pilihanMenu = int(input("Silahkan pilih menu yang diinginkan: "))
    if pilihanMenu == 1:
        print("Menampilkan daftar menu kopi...")
        print(daftarMenu)
    elif pilihanMenu == 2:
        print("Menu apa yang ingin ditambahkan?")
        indexTambah = int(input("Item keberapa ini: "))
        tambahMenu = input("Masukkan nama menu yang ingin ditambahkan: ")
        tambahStok = int(input("Masukkan stok yang ditambahkan: "))
        tambahHargaMenu = int(input("Masukkan harga yang diinginkan: "))
        daftarMenu.add_row([indexTambah,tambahMenu, tambahStok,tambahHargaMenu])
        print(daftarMenu)
    elif pilihanMenu == 3:
        print("Menu apa yang ingin dihapus?")
        hapusMenu = int(input("Masukkan menu yang ingin dihapus: "))
        print(daftarMenu)
        confirm = input("Yakin ingin menghapusnya? (Y/N)")
        if confirm == "Y" or confirm == "y" :
            daftarMenu.del_row(hapusMenu)
        else :
            print("Baiklah kalau tidak jadi!")
        print(daftarMenu)

    elif pilihanMenu == 4:
        print("Silahkan pilih dari menu berikut.")
        print(daftarMenu)
        try:
            indexPilihan = int(input("Masukkan di angka berapa menu itu berada: "))
            jumlahBeli = int(input("Masukkan jumlah yang diinginkan: "))
            if indexPilihan < len(daftarMenu.rows) and jumlahBeli <= daftarMenu.rows[indexPilihan][2]:
                daftarMenu.rows[indexPilihan][2] -= jumlahBeli
                totalHarga = jumlahBeli * daftarMenu.rows[indexPilihan][3]
                print(f"Total pembelian: {totalHarga}")
                uangDibayar = int(input("Silahkan lakukan pembayaran: "))
                if uangDibayar == totalHarga:
                    print("Pembayaran berhasil! Selamat menikmati kopi anda.")
                elif uangDibayar > totalHarga:
                    kembalian = uangDibayar - totalHarga
                    print(f"Pembayaran berhasil! kembalian anda {kembalian}. Selamat menikmati kopi anda.")
                else:
                    print("Mohon maaf pembayaran anda kurang. Harap masukkan jumlah yang sesuai")
                    jumlahKurang = totalHarga - uangDibayar
                    print(f"Jumlah yang kurang: {jumlahKurang}")
                    uangKurang = int(input("Masukkan pembayaran anda yang kurang: "))
                    kembalian = uangKurang - uangKurang
                    if uangKurang > jumlahKurang:
                        print(f"Pembayaran berhasil! kembalian anda {kembalian}. Selamat menikmati kopi anda.")
                    elif jumlahKurang == uangKurang:
                        print("Pembayaran berhasil! Selamat menikmati kopi anda.")
                    else:
                        print("Transaksi dibatalkan")
            else:
                print("Jumlah yang diminta melebihi stok atau menu tidak ada!")
        except ValueError:
            print("Input tidak valid pastikan anda menggunakan angka!")


    elif pilihanMenu == 5:
        print("Terima kasih telah memakai program ini.")
        break

    else :
        print("Pilihan tidak tersedia.")
