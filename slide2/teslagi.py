apel = 5
anggur = 7
jeruk = 8

hargaApel = 10000
hargaAnggur = 15000
hargaJeruk = 20000

jumlahBuahApel = input("Masukkan jumlah Apel yang anda inginkan : ")
jumlahBuahApel = int(jumlahBuahApel)
if(jumlahBuahApel > apel):
    jumlahBuahApel = 0
    print(f"Kesalahan Dalam input, Stock Apel {apel} buah")
else:
    apel = apel - jumlahBuahApel

jumlahBuahAnggur = input("Masukkan jumlah Anggur yang anda inginkan : ")
jumlahBuahAnggur = int(jumlahBuahAnggur)
if(jumlahBuahAnggur > anggur):
    jumlahBuahAnggur = 0
    print(f"Kesalahan Dalam input, StockAnggur {anggur} buah")
else:
    anggur = anggur - jumlahBuahAnggur

jumlahBuahJeruk = input("Masukkan jumlah Jeruk yang anda inginkan : ")
jumlahBuahJeruk = int(jumlahBuahJeruk)
if(jumlahBuahJeruk > jeruk):
    jumlahBuahJeruk = 0
    print(f"Kesalahan Dalam input, Stock Jeruk {jeruk} buah")
else:
    jeruk = jeruk - jumlahBuahJeruk

beliApel = jumlahBuahApel * hargaApel
beliAnggur = jumlahBuahAnggur * hargaAnggur
beliJeruk = jumlahBuahJeruk * hargaJeruk
totalHarga = beliApel + beliAnggur + beliJeruk

print("")
print("        NOTA")
print(f"")
print(f"Apel {jumlahBuahApel} x {hargaApel} = {beliApel}")
print(f"Anggur {jumlahBuahAnggur} x {hargaAnggur} = {beliAnggur}")
print(f"Jeruk {jumlahBuahJeruk} x {hargaJeruk} = {beliJeruk}")
print("")
print(f"Total Harga = {totalHarga}")

# print(f" \n        NOTA \n Apel {jumlahBuahApel} x {hargaApel} = {beliApel}\n Anggur {jumlahBuahAnggur} x {hargaAnggur} = {beliAnggur}\n Jeruk {jumlahBuahJeruk} x {hargaJeruk} = {beliJeruk} \n Total Harga = {totalHarga}")