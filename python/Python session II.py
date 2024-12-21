# loop statement


# while loop
angka = int(input("Ketik angka lebih dari 8 anda: "))

while angka > 8:
    print("bagus!")
print("angka itu lebih kecil dari 8!")


i = 2
while i in range(20):
    i += 2
    print(f"Hitung ke-({i})")
print("Selesai")


#tanpa angka
i = input("apakah anda ingin memulai: ")
while i == 'Y':
    print("Memulai...")
    i = input("apakah anda ingin mengulang: ")
print('selesai')


# for loop


for i in range(0,11,1):
    i += 1
    print(f"angka-{i}")
print("selesai")


n = 0
    
while n in range(5):
    while n == 2:
        break
    print(n)


i = 0
while i in range(5):
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    
    
    
stars =' '
size = 5
for i in range(5, 0, -1):
    for j in range(-1 + i):
        
        
        
        


# list tuple dan python data type lainnya

listContoh = ['hello', 1, 1, 3, True] # ini error karena sudah diubah dibawah
print(listContoh)
listContoh[1]= 'test'
listContoh[3]= 'coba'
print(listContoh)
listContoh.insert(2,'boleh')
print(listContoh)
del listContoh[2]
print(listContoh)
listContoh
#menambahkan fungsi loop di file tipe list
for item in listContoh:
    print(item)
print(listContoh,type(listContoh))

listContoh = ['hello', 'test', 1, 'coba', True]
newList1 = listContoh
print(newList1)
newList1[2,'baru nih']
print(newList1)



# listAnyar2D = [
 #   ['buku':'novel'], ['tv':'monitor'], ['pulpen':'spidol']
 #   ]

# nomor 2
jmlApel = int(input("Masukkan Jumlah apel: "))
jmlJeruk = int(input("Masukkan jumlah Jeruk: "))
while i in jmlJeruk > 8:
    print()
    
    


# nomor 3
numbers = [41, 5, 1, 3, 89, 32]
numbers.sort()
print(numbers)
print(f'minimum value: {numbers[0]}')
print(f'Maximum value: {numbers[5]}')

# nomor 4
listSebelumDiSort = [41,5,1,3,89,32]
listSebelumDiSort.sort()
listSesudahDiSort = listSebelumDiSort
print(listSesudahDiSort)





# nomor 5

listMenu = []