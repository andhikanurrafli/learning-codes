# membuat sebuah program penghitungan material di genshin impact
# material yang dihitung adalah material yang dibutuhkan untuk menaikan karakter

# material yang dibutuhkan untuk ascend character ke level 90

# buku exp
bukuLv3Needed = 419
bukuLv2Needed = bukuLv3Needed * 3
bukuLv1Needed = bukuLv2Needed * 3

# gem ascension
gemLv4Needed = 6
gemLv3Needed = 9
gemLv2Needed = 9
gemLv1Needed = 1

# buku talent
talentLv3Needed = 114
talentLv2Needed = 63
talentLv1Needed = 9

# speciality yang dibutuhkan
specialityNeeded = 168

# material bos
bosMaterialNeeded = 46

# material musuh
mobMaterialLv3Needed = 129
mobMaterialLv2Needed = 96
mobMaterialLv1Needed = 36

# material bos mingguan
weeklyBosNeeded = 18

# crown
crownNeeded = 3

# mora 
moraNeeded = 7_049_000

# membuat list menu

print("Selamat datang di program penghitungan material di Genshin Impact")
print("Berikut adalah menu yang tersedia: ")

listMenuProgram = ["1. Menghitung Buku exp", "2. Menghitung Gem Ascension", "3. Menghitung Buku Talent", 
                   "4. Menghitung Speciality", "5. Menghitung Material Bos", "6. Menghitung Material Musuh", 
                   "7. Menghitung Material Bos Mingguan", "8. Menghitung Crown", "9. Menghitung Mora"]
for n in listMenuProgram:
    print(n)
    
pilihanMenu = int(input("Masukkan pilihan menu: "))
while True: 
    if pilihanMenu == 1:
        bukuLv3 = int(input("Masukkan jumlah buku level 3 yang ada: "))
        bukuLv2 = int(input("Masukkan jumlah buku level 2 yang ada: "))
        bukuLv1 = int(input("Masukkan jumlah buku level 1 yang ada: "))
        
    elif pilihanMenu == 2:
        gemLv3 = int(input("Masukkan jumlah gem level 3 yang ada: "))
        gemLv2 = int(input("Masukkan jumlah gem level 2 yang ada: "))
        gemLv1 = int(input("Masukkan jumlah gem level 1 yang ada: "))
        
    elif pilihanMenu == 3:
        talentLv3 = int(input("Masukkan jumlah talent level 3 yang ada: "))
        talentLv2 = int(input("Masukkan jumlah talent level 2 yang ada: "))
        talentLv1 = int(input("Masukkan jumlah talent level 1 yang ada: "))
        
    elif pilihanMenu == 4:
        speciality = int(input("Masukkan jumlah speciality yang ada: "))
        if speciality == specialityNeeded:
            print("Speciality anda sudah cukup")
        elif speciality > specialityNeeded:
            specialityLebih = speciality - specialityNeeded
            print(f"Speciality anda berlebih sebanyak {specialityLebih}")
        else:
            specialityKurang = specialityNeeded - speciality
            print(f"Speciality anda kurang sebanyak {specialityKurang}")   
        
    elif pilihanMenu == 5:
        bosMaterial = int(input("Masukkan jumlah material bos yang ada: "))
        
    elif pilihanMenu == 6:
        mobMaterialLv3 = int(input("Masukkan jumlah material musuh level 3 yang ada: "))
        mobMaterialLv2 = int(input("Masukkan jumlah material musuh level 2 yang ada: "))
        mobMaterialLv1 = int(input("Masukkan jumlah material musuh level 1 yang ada: "))
        if mobMaterialLv3 == mobMaterialLv3Needed or mobMaterialLv2 == mobMaterialLv3Needed * 3 == mobMaterialLv1 / 9:
            print("Material musuh level 3 sudah cukup")
        elif  mobMaterialLv3 > mobMaterialLv3Needed or mobMaterialLv2 > mobMaterialLv2Needed or mobMaterialLv1 > mobMaterialLv1Needed:
            mobMaterialLv3Lebih = mobMaterialLv3 - mobMaterialLv3Needed
            mobMaterialLv2Lebih = mobMaterialLv2 - mobMaterialLv2Needed
            mobMaterialLv1Lebih = mobMaterialLv1 - mobMaterialLv1Needed
            print(f"Material musuh level 3 berlebih sebanyak {mobMaterialLv3Lebih}")
            print(f"Material musuh level 2 berlebih sebanyak {mobMaterialLv2Lebih}")
            print(f"Material musuh level 1 berlebih sebanyak {mobMaterialLv1Lebih}")
        else:
            mobMaterialLv3Kurang = mobMaterialLv3Needed - mobMaterialLv3
            mobMaterialLv2Kurang = mobMaterialLv2Needed - mobMaterialLv2
            mobMaterialLv1Kurang = mobMaterialLv1Needed - mobMaterialLv1
            print(f"Material musuh level 3 kurang sebanyak {mobMaterialLv3Kurang}")
            print(f"Material musuh level 2 kurang sebanyak {mobMaterialLv2Kurang}")
            print(f"Material musuh level 1 kurang sebanyak {mobMaterialLv1Kurang}")
            
        
    elif pilihanMenu == 7:
        weeklyBos = int(input("Masukkan jumlah weekly bos yang ada: "))
        if weeklyBos == weeklyBosNeeded:
            print("Weekly bos anda sudah cukup")
        elif weeklyBos > weeklyBosNeeded:
            weeklyBosLebih = weeklyBos - weeklyBosNeeded
            print(f"Weekly bos anda berlebih sebanyak {weeklyBosLebih}")
        else:
            weeklyBosKurang = weeklyBosNeeded - weeklyBos
            print(f"Weekly bos anda kurang sebanyak {weeklyBosKurang}")
        
    elif pilihanMenu == 8:
        crown = int(input("Masukkan jumlah crown yang ada: "))
        if crown == crownNeeded:
            print("Crown anda sudah cukup")
        elif crown > crownNeeded:
            crownLebih = crown - crownNeeded
            print(f"Crown anda berlebih sebanyak {crownLebih}")
        else:
            crownKurang = crownNeeded - crown
            print(f"Crown anda kurang sebanyak {crownKurang}")
        
    elif pilihanMenu == 9:
        mora = int(input("Masukkan jumlah mora yang ada: "))
        if mora == moraNeeded:
            print("Mora anda sudah cukup")
        elif mora > moraNeeded:
            moraLebih = mora - moraNeeded
            print(f"Mora anda berlebih sebanyak {moraLebih}")
        else:
            moraKurang = moraNeeded - mora
            print(f"Mora anda kurang sebanyak {moraKurang}")
        
    else:
        print("Menu tidak tersedia")
        break



# user input
# 1 buku exp


# 2 gem untuk ascension


# 3 buku talent


# 4 speciality


# 5 material bos


# 6 material musuh


# 7 membuat struktur kodenya

# 8 untuk menghitung 

