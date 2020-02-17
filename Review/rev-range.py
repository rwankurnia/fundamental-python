# RANGE 
# Sebuah fuction yang aka me return list of integer
# Range menerima 1 parameter wajib, 2 parameter tidak wajib

# Menerima 1 parameter
# Parameter tersebut digunakan sebagai batas akhir angka
# Angka pertama dimulai dari 0
resRange = list(range(5))
print(resRange) # [0, 1, 2, 3, 4]

# Menerima 2 parameter
# Parameter 1 : nilai awal
# Parameter 2 : nilai akhir (tidak termasuk)
resRange = list(range(2, 7))
print(resRange) # [2, 3, 4, 5, 6]

# Menerima 3 parameter
# Parameter 1 : nilai awal
# Parameter 2 : nilai akhir (tidak termasuk)
# Parameter 3 : step, Loncatan setiap nilai (default :1)
resRange = list(range(2, 15, 2))
print(resRange) # [2, 4, 6, 8, 10, 12, 14]

resRange = list(range(10, 1, -1))
print(resRange) # [10, 9, 8, 7, 6, 5, 4, 3, 2]

resRange = list(range(10, 1, -2))
print(resRange) # [10, 8, 6, 4, 2]


days = ['Sunday', 'Monday', 'Tuesday']

# looping sebanyak data yang ada di days : 3
# [0, 1, 2]
for i in range(len(days)):
    print(f'Loop i : {i}')