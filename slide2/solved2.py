# berat = input("Masukkan Massa(kg) : ")
# tinggi = input("Masukkan Tinggi(cm) : ")
# tinggim = float(tinggi) / 100

# ideal = float(berat) / (tinggim ** 2)

# print(f"Massa {berat} kg & Tinggi {tinggim} m ")

# if ideal < 18.5 :
#     print(f"IMT = {ideal}, BERAT BADAN KURANG")
# elif ideal >= 18.5 and ideal <= 24.9 :
#     print(f"IMT = {ideal}, BERAT BADAN IDEAL")
# elif ideal >= 25.0 and ideal <= 29.9 :
#     print(f"IMT = {ideal}, BERAT BADAN BERLEBIH")
# elif ideal >= 30.9 and ideal <= 39.9 :
#     print(f"IMT = {ideal}, BERAT BADAN SANGAT BERLEBIH")
# else :
#     print(f"IMT = {ideal}, BERAT BADAN OBESITAS")


#Cara ke 2
berat = int(input("Masukkan Massa(kg) : "))
tinggi = int(input("Masukkan Tinggi(cm) : "))
tinggim = tinggi / 100

ideal = berat / pow(tinggim, 2) #pow adalah kuadrat

print(f"Massa {berat} kg & Tinggi {tinggim} m ")

if ideal < 18.5 :
    print(f"IMT = {ideal}, BERAT BADAN KURANG")
elif ideal >= 18.5 and ideal <= 24.9 :
    print(f"IMT = {ideal}, BERAT BADAN IDEAL")
elif ideal >= 25.0 and ideal <= 29.9 :
    print(f"IMT = {ideal}, BERAT BADAN BERLEBIH")
elif ideal >= 30.9 and ideal <= 39.9 :
    print(f"IMT = {ideal}, BERAT BADAN SANGAT BERLEBIH")
else :
    print(f"IMT = {ideal}, BERAT BADAN OBESITAS")