banyakHari = 485

tahun = int(banyakHari / 360)
hari = banyakHari % 360

bulan = int(hari / 30)
hari = hari % 30

minggu = int(hari / 7)
hari = hari % 7

# print(str(tahun) + " Tahun " + str(bulan) + " Bulan " + str(minggu) + " Minggu " + str(hari) + " Hari ") 
# print(f" {tahun} Tahun {bulan} Bulan {minggu} Minggu {hari} Hari ") 
print(f" Total {banyakHari} hari ")
print(f" {tahun} Tahun ") 
print(f" {bulan} Bulan ") 
print(f" {minggu} Minggu ") 
print(f" {hari} Hari ") 
