# # DICTIONARY
# # Menggunakan kurung kurawal {}
# # Tidak menggunakan index, melainkan property
# # Nama property ditulis menggunakan kutip (seperti string)

# price = {
#     "apple" : 10000,
#     "grape" : 15000,
#     "orange" : 15000
# }

# price["grape"] // 15000

# print(price["grape"])  ## 15000

# ================================

# d = {
#     "numInt" : 123,
#     "numList" : [0, 1, 2],
#     "numStr" : "Hello",
#     "numDict" : {"insideKey" : 100}

# }

# print(d["numList"])  ## [0, 1, 2]
# print(d["numDict"])  ## {'insideKey': 100}
# print(d["numDict"]["insideKey"])  ## 100
# print(d["numList"][2])  ## 2

# # =================================

heroes = {
    "batman" : {"name" : "Bruce", "age" : 41},
    "ironman" : {"name" : "Tony", "age" : 42},
    "thor" : {"name" : "Thor", "age" : 39}
}

# heroes["ironman"]
# heroes["ironman"]["name"]

# KEYS
# Untuk mendapatkan semua keys dari dictionary
keys = heroes.keys()

# keys # dict_keys("batman", "ironman", "thor")

for i in keys:
    print(i)

# #=============================================

# # VALUES
# # Untuk mendapatkan semua value dari dictionary
# heroes = {
#     "batman" : {"name" : "Bruce", "age" : 41},
#     "ironman" : {"name" : "Tony", "age" : 42},
#     "thor" : {"name" : "Thor", "age" : 39}
# }

# values = heroes.values()

# # i = ("name" : "Bruce", "age" : 41)
# for i in values:
#     print(
#         "Name: " + i["name"]
#     )

#==========================

# # TUPLE
# # Mengunakan kurung ()
# # Mengenal indexing, dimulai dari 0
# # Nilainya tidak dapat dirubah
# colorTpl = ("red", "green", "blue", "green", "blue")

# colorTpl[1] # Green
# colorTpl[-1] # Blue

# # Error, tidak bisa merubah nilai tuple
# # colorTpl[0] = "Merah"

# # Count
# # Menghitung banyak data pada tuple
# count = colorTpl.count("green") #2

# print(f"Jumlah warna hijau : {count}")

# # Index
# # Mencari index data tertentu
# index = colorTpl.index("blue")
# print(f"Index warna blue :  {index}")

# Persons

# persons = (
#     {"name" : "John", "job" : "Assassins"},
#     {"name" : "Bruce", "job" : "Hunter"},
#     {"name" : "Jajang", "job" : "OB"}
# )

# persons[1]["name"] = "BruceLee"

# print(persons[1])