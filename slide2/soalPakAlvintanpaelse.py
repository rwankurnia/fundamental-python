# apel = 5
# anggur = 7
# jeruk = 8

# hargaApel = 10000
# hargaAnggur = 15000
# hargaJeruk = 20000

# jumlahBuahApel = int(input("Masukkan jumlah Apel yang anda inginkan : "))
# if(jumlahBuahApel > apel):
#     jumlahBuahApel = 0
#     print(f"Kesalahan Dalam input, Stock Apel {apel} buah")

# jumlahBuahAnggur = int(input("Masukkan jumlah Anggur yang anda inginkan : "))
# if(jumlahBuahAnggur > anggur):
#     jumlahBuahAnggur = 0
#     print(f"Kesalahan Dalam input, StockAnggur {anggur} buah")

# jumlahBuahJeruk = int(input("Masukkan jumlah Jeruk yang anda inginkan : "))
# if(jumlahBuahJeruk > jeruk):
#     jumlahBuahJeruk = 0
#     print(f"Kesalahan Dalam input, Stock Jeruk {jeruk} buah")

# beliApel = jumlahBuahApel * hargaApel
# beliAnggur = jumlahBuahAnggur * hargaAnggur
# beliJeruk = jumlahBuahJeruk * hargaJeruk
# totalHarga = beliApel + beliAnggur + beliJeruk

# print("")
# print("        NOTA")
# print(f"")
# print(f"Apel {jumlahBuahApel} x {hargaApel} = {beliApel}")
# print(f"Anggur {jumlahBuahAnggur} x {hargaAnggur} = {beliAnggur}")
# print(f"Jeruk {jumlahBuahJeruk} x {hargaJeruk} = {beliJeruk}")
# print("")
# print(f"Total Harga = {totalHarga}")

# print(f" \n        NOTA \n Apel {jumlahBuahApel} x {hargaApel} = {beliApel}\n Anggur {jumlahBuahAnggur} x {hargaAnggur} = {beliAnggur}\n Jeruk {jumlahBuahJeruk} x {hargaJeruk} = {beliJeruk} \n Total Harga = {totalHarga}")

apel = 5
anggur = 7
jeruk = 8

hargaApel = 10000
hargaAnggur = 15000
hargaJeruk = 20000

inputApel = int(input("Masukkan jumlah apel : "))
while inputApel > apel:
    inputApel = int(input(f"Kesalahan Dalam input, Stock Apel {apel} buah \nMasukkan kembali jumlah apel : "))
    if inputApel <= apel:
        break

inputAnggur = int(input("Masukkan jumlah anggur : "))
while inputAnggur > anggur:
    inputAnggur = int(input(f"Kesalahan Dalam input, Stock Anggur {anggur} buah \nMasukkan kembali jumlah anggur : "))
    if inputAnggur <= anggur:
        break

inputJeruk = int(input("Masukkan jumlah apel : "))
while inputJeruk > jeruk:
    inputJeruk = int(input(f"Kesalahan Dalam input, Stock Jeruk {jeruk} buah \nMasukkan kembali jumlah jeruk : "))
    if inputJeruk <= jeruk:
        break

beliApel = inputApel * hargaApel
beliAnggur = inputAnggur * hargaAnggur
beliJeruk = inputJeruk * hargaJeruk
totalHarga = beliApel + beliAnggur + beliJeruk

inputBayar = int(input("Input Uang anda : "))
while inputBayar < totalHarga:
    inputBayar = int(input(f"Uang Anda Kurang dari {totalHarga} \nMasukkan ulang Uang Anda : "))
    if inputBayar > totalHarga:
        sisaBayar = inputBayar - totalHarga
        print(f"Terima Kasih, Kembalian Anda {sisaBayar} ")
    else:
        print(f"Terima Kasih, Uang Anda Pas \nSilahkan Datang Kembali")