
# dasar-dasar

print('Hello teman-teman semua, selamat bergabung di Purwadhika!')
print(1 + 77**3)
x = 21
y = 2345
print(x**y + 2345)
sum(x)


# mencoba membuat contoh variable
pesan = "Terima kasih sudah datang"
sambutan = "Halo teman-teman semua, selamat bergabung di Purwadhika!" 
    # variable hanya membaca data yang paling terbaru dari pembuatan variable itu
latihan = "Mencoba python part 1"
    # contoh
dompet = "Alat untuk menyimpan duit"
print(dompet)
dompet = "Banyak duit"
print(dompet)

print(pesan)
print(sambutan)
print(latihan)
print(latihan)

# jenis data

x = "Hello purwadhika" ## string bisa make kutip 1 juga, pokoknya harus ada tanda kutip


x = None ## none
print(x)


x = range(7) ## range

xDataType = type(x)
print(x)


# method math

import math
print(22/7)
math.floor(22/7)
math.pi

# python casting

angkaStr = "1234"
angkaInt = 123/2
angkaFloat = 123/2

int(angkaStr)
print(angkaStr/2)

# escape character

txt = "Salam kenal murid \"Purwadhika\", mari kita belajar bersama."
print(txt)



# len function and string
x1 = 'Halo Dunia'

print(len(x1))

panjangString = len(x1)
indexDunia = x1.index('Dunia')
print(indexDunia)
hasilSplit = x1.split(' ')
print(hasilSplit)
jadiHurufKecil = x1.lower()
print(jadiHurufKecil)
jadiHurufBesar = x1.upper()
print(jadiHurufBesar)
hurufPertamaKapital = x1.capitalize()
print(hurufPertamaKapital)

# string slicing
text = "I'm Baron nice to meet you"
print(text[10:14])


# concate 

a = "apel"
b = "jeruk"
c = a + " " + b
print(c)
print(c, str(234))


# string format
jumlahApel = 3
jumlahJeruk = 5
pembelian = "saya mau beli {} apel, {} mangga, dan {} jeruk "
print(pembelian.format(jumlahApel, 7, jumlahJeruk))



# input function
username = input("Masukkan username:")
print("Username anda: " + username)

# boolean and logical operator

23 >= 22

umur = input('Masukkan umur anda: ')

if umur >=17:
    print('eligible')

else :
    print('not eligible')

