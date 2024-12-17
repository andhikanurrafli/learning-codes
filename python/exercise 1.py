# nomor 1

x = 4
y = 3
z = 2
a = x + (y*z)
b = x*y
c = a/b
d = c**z
print(d)

# nomor 2

kuadrat = int(input('masukkan angka: '))
hasil = kuadrat**2
print('kuadrat dari bilangan itu adalah')
print(hasil)


# nomor 3

hari = 1 + "hari"
bulan = 30 + "hari"
tahun = 360 + "hari"

# kode (meta ai)
def konversi_hari(hari):
    tahun = hari // 360
    sisa_hari = hari % 360
    bulan = sisa_hari // 30
    sisa_hari = sisa_hari % 30
    minggu = sisa_hari // 7
    hari = sisa_hari % 7
    
    return tahun, bulan, minggu, hari

hari = 485
tahun, bulan, minggu, hari = konversi_hari(hari)

print(f"{hari} hari sama dengan:")
print(f"Tahun: {tahun}")
print(f"Bulan: {bulan}")
print(f"Minggu: {minggu}")
print(f"Hari: {hari}")

# kode (meta ai)
hari = 485

tahun = hari // 360
sisa_hari = hari % 360

bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30

minggu = sisa_hari // 7
hari = sisa_hari % 7

print(f"{485} hari sama dengan:")
print(f"Tahun: {tahun}")
print(f"Bulan: {bulan}")
print(f"Minggu: {minggu}")
print(f"Hari: {hari}")

## user input (meta ai)
def konversi_hari():
    hari = int(input("Masukkan jumlah hari: "))

    tahun = hari // 360
    sisa_hari = hari % 360
    bulan = sisa_hari // 30
    sisa_hari = sisa_hari % 30
    minggu = sisa_hari // 7
    hari = sisa_hari % 7

    print(f"{hari} hari sama dengan:")
    print(f"Tahun: {tahun}")
    print(f"Bulan: {bulan}")
    print(f"Minggu: {minggu}")
    print(f"Hari: {hari}")

## Jalankan Fungsi
konversi_hari()



# nomor 4
total_usia = 49
rasio_andi_budi = 0.4

budi_usia = total_usia / (1 + rasio_andi_budi)
andi_usia = total_usia - budi_usia

print("Usia Andi saat ini:", round(andi_usia))
print("Usia Budi saat ini:", round(budi_usia))
print("Usia Andi 2 tahun lagi:", round(andi_usia) + 2)
print("Usia Budi 2 tahun lagi:", round(budi_usia) + 2)

# nomor 5

d0 = 120 # km
va = 60 # km/h
vb = 40 # km/h
vRel = va + vb # km/h
waktuJalan = 9 # jam


t = d0/vRel # jam
jamBertemu, menitBertemu = divmod(t * 60,60)

pukulTabrakanJam = waktuJalan + int(jamBertemu)
pukulTabrakanMenit = int(menitBertemu)

print(f"A dan B akan bertabrakan pukul {pukulTabrakanJam:02D}:{pukulTabrakanMenit:02d} WIB.")

## chatgpt kode
# Diketahui
jarak_awal = 120  # km
kecepatan_a = 60  # km/jam
kecepatan_b = 40  # km/jam
waktu_mulai = 9  # Pukul 9:00 WIB

# Hitung kecepatan relatif
kecepatan_relatif = kecepatan_a + kecepatan_b  # karena saling mendekat

# Hitung waktu bertemu (dalam jam)
waktu_bertemu = jarak_awal / kecepatan_relatif

# Konversi waktu bertemu ke jam dan menit menggunakan divmod
jam_bertemu, menit_bertemu = divmod(waktu_bertemu * 60, 60)

# Hitung waktu tabrakan
pukul_tabrakan_jam = waktu_mulai + int(jam_bertemu)
pukul_tabrakan_menit = int(menit_bertemu)

# Tampilkan hasil
print(f"A dan B akan bertabrakan pada pukul {pukul_tabrakan_jam:02d}:{pukul_tabrakan_menit:02d} WIB.")




# nomor 6
jmlApel = int(input("Masukkan Jumlah Apel: "))
jmlJeruk = int(input("Masukkan Jumlah Jeruk: "))
jmlAnggur = int(input("Masukkan Jumlah Anggur"))
total = (jmlApel*10000) + (jmlJeruk*15000) + (jmlAnggur*20000)
detailBelanja = "Apel {} x 10000, Jeruk {} x 15000, Anggur {} x 20000"
print(detailBelanja.format(jmlApel,jmlJeruk,jmlAnggur))
print("Total: " + str(total) )


# nomor 7

angka = int(input("Masukkan angka: "))
hasil = angka % 2
if hasil == 0 :
    print(str(angka) + " " + "tergolong bilangan Genap!")
else :
    print(str(angka) + " " + "tergolong bilangan Ganjil!")



# nomor 8

beratBadan = int(input("Masukkan berat badan (kg): "))
tinggi = int(input("Masukkan tinggi badan (cm): ")) 
tinggiMeter = tinggi/100
print("Berat badan"+ " "+ str(beratBadan) + " " +"dan tinggi"+ " "+ str(tinggi/100))
imt = beratBadan/(tinggiMeter**2)

if imt < 18.5 :
    print("Berat badan kurang")
elif imt >= 18.5 :
    print("Berat badan ideal")
elif imt >= 25.0 :
    print("Berat badan berlebih")
elif imt >= 30.0 :
    print("Berat badan sangat berlebih")
else :
    print("Obesitas")

print("IMT anda adalah"+ " " + str(imt))

# nomor 9
jmlApel = int(input("Masukkan Jumlah Apel: "))
jmlJeruk = int(input("Masukkan Jumlah Jeruk: "))
jmlAnggur = int(input("Masukkan Jumlah Anggur"))
total = (jmlApel*10000) + (jmlJeruk*15000) + (jmlAnggur*20000)
detailBelanja = "Apel {} x Rp. 10000, Jeruk {} x Rp. 15000, Anggur {} x Rp. 20000"
print(detailBelanja.format(jmlApel,jmlJeruk,jmlAnggur))
print("Total: Rp. " + str(total) )
cash = int(input("Masukkan jumlah uang: "))
print("Uang anda: Rp. "+ str(cash))
if cash > total :
    print("Terima kasih telah berbelanja kembalian anda:"+ str(cash - total))
elif cash == total :
    print("Terima kasih telah berbelanja!")
else: 
    print("Transaksi dibatalkan! Uang anda kurang: Rp. " + str(total - cash))





cash = input("Masukkan jumlah uang: ")
print(str(cash))
