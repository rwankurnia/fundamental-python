
# apel = 5
# anggur = 7
# jeruk = 8

# hargaApel = 10000
# hargaAnggur = 15000
# hargaJeruk = 20000


fruits = ['Apel', 'Anggur', 'Jeruk']
stock = [5, 7, 8]
price = [1000, 15000, 20000]

#TUGAS : 
    # Memiliki menu utama:
    # 1. Melihat List Buah (name | Stock | Price)
    # 2. Menambahkan list Buah
    # 3. Belanja Buah

    # Hanya ada satu while dalam input qty semua Buah
    # Setiap selesai menambahkan buah, tampilkan list buah terbaru

centerMenu =  int(input(
    "Pilih Menu yang anda butuhkan : 1. Melihat List Buah  2. Menambahkan List Buah 3. Belanja Buah : "))
if centerMenu == 1 :
    print("a")
elif centerMenu == 2 :
    print("b")
else:
    print("c")