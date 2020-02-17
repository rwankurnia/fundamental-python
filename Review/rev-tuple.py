# TUPLE
# Menggunakan kurung ()
# Akses value menggunakan index

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "friday")

# Access one value
days[0] # Sunday
days[1] # Monday
days[0] # Friday

# More than one value
days[1:4] # ("Monday", "Tuesday", "Wednesday")
print(days[1:4]) # ("Monday", "Tuesday", "Wednesday")

# Count
# Menghitung jumlah value tertentu pada tuple
days.count("Sunday") # 2
print(days.count("Sunday")) # 2

# index
# Mencari index dari suatu value pada tuple
days.index("Tuesday") # 3

# ... in ...
# Cek apakah suatu value ada didalam tuple, return true / false
"Saturday" in days # False
print("Saturday" in days)

# for ... in ...
# loop terhadap semua data yang ada di list
for day in days:
    print(f"Today is {day}")