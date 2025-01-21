import math  #import fungsi(?)

satu = 1


print(satu)
print("You've succesfully run a python code")

alice_candies = 121
bob_candies = 77
carol_candies = 109

math.ceil(alice_candies)

x001 = math.sqrt(carol_candies)

print(x001)

x00 = math.pi

print(x00)

to_smash = (alice_candies + bob_candies + carol_candies) %  3

print(to_smash)
print(to_smash + 2)

x = "Aku String"
xDataType = type(x)
print(xDataType)

x0 = {"Jeruk", "Apel", "Mangga"}

kutipSatu = 'Kutip Satu ("Im Batman")'
kutipDua = "Kutip Dua (I'm Iron Man)"
kutipTiga = ''' 
    "Im Batman"
    I'm Iron Man
'''

print(kutipSatu)
print(kutipDua)
print(kutipTiga)

txt = "Salam kenal murid \"Purwadhika\", mari kita belajar bersama."
print(txt)

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

text = "I'm Baron nice to meet you"
print(text[10:14])

username = input("Masukkan username:")
print("Username anda: " + username)

x = 4
y = 3
z = 2

# loop statement learning

## menggunakan while
i = 1 # disini dimulai angkanya

while i <= 8: # tentukan mau di loop sampe berapa kali
    print(f"Angka ke-{i}") # output yang diinginkan
    i += 1 # gapnya mau dibuat berapa

### contoh lain

userInput = " "

while userInput.lower() != "stop":
    userInput = input("Ketik sesuatu (Atau 'stop' untuk berhenti): ")
    if userInput.lower() != "stop":
        print(f"Kamu mengetik: {userInput}")

print("Program berhenti")


n = int(input("Masukkan angka yang ingin di faktorialkan: "))
faktorial = 1

while n > 0:
    faktorial *= n
    n -= 1

print(f"Faktorialnya adalah: " + str(faktorial))

## menggunakan for 
### menyebutkan range angka

for i in range(1, 9):  # disini variable nya udah masuk kedalam rumus
    print(f"angka ke-{i}") # fungsi print yang mengikuti variable

### contoh lain seperti sapaan

nama = ["freya", "gracia", "christy"]

for n in nama:
    print(f"Hallo, {n}!")

### contoh lain: penyebutan huruf

kata = "sugar rush"

for huruf in kata:
    print(huruf)

### lain dictionary

data = {"nama": "gracia", "usia": "25", "kota":"bekasi"}

for kunci, nilai in data.items():
    print(f"{kunci}: {nilai}")

### nested 

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("---")


### try try
for i in range(1,11):
    print(i)



### stars exercise 1

stars ='* '
size = 5

for i in range(size):
    for j in range(5 - i):
        stars += '* '
    stars += '\n'

print(stars)

for i in range(size):
    for j in range(1 + i):
        stars += '* '
    stars += '\n'\

print(stars)
##### bentuk 1
stars = ' '
size = 5

for i in range(size):
    for j in range(5 - i):
        stars += ' *'
    stars += '\n'



for i in range(size):
    for j in range(1 + i):
        stars += ' *'
    stars += '\n'

print(stars)

##### bentuk 2
stars = ' '
size = 10

for i in range(size):
    for j in range(1 + i):
        stars += '* '
    stars += '\n'


for i in range(size):
    for j in range(10 - i):
        stars += '* '
    stars += '\n'

print(stars)



def salamBalik(nama,usia) :
    print("Hello perkenalkan nama saya {}, dan usia saya {}".format(nama,usia))
    print('Senang bertemu dengan anda!')

salamBalik("Gracia", 25)
salamBalik("Freya", 25)
salamBalik("Christy", 25)
