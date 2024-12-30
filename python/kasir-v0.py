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
