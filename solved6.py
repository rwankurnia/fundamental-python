# jarakMobil = 120
# a = 60
# b = 40

# jamMulai = 9

# waktuPapasan = 120/(a + b)
# # print(waktuPapasan)
# menitPapasan = waktuPapasan * 60 
# # print(menitPapasan)

# jamPapasan = int(waktuPapasan)
# print("Mereka Berpapasan  " + str(jamPapasan))


bentuk = input("Masukkan bentuk yang anda inginkan : 1. Persegi  2. segitiga siku 3. Segitiga sama kaki : ")
if(bentuk == "1"):
    persegi = int(input("Masukkan panjang persegi yang anda inginkan : "))
    z=" "
    for item in range(persegi):       # for dalam for (2x looping atau 2x perulangan)
        for item1 in range(persegi):
            z += " * "              
        z += " \n "   
    print(z)
elif(bentuk == "2"):
    segitigasiku = input("Masukkan segitiga siku yang anda inginkan : 1. Segitiga Siku Atas 2. Segitiga Siku Bawah : ")
    if(segitigasiku == "1"):
        segitigasiku1 = int(input("Masukkan Panjang Segitiga Siku Atas : "))
        z=" "
        for item in range(segitigasiku1):       # for dalam for (2x looping atau 2x perulangan)
            for item1 in range(0, item+1):
                z += " * "
            z += " \n "              #\n berfungsi sebagai enter
        print(z)  
    elif(segitigasiku == "2"):
        segitigasiku1 = int(input("Masukkan Panjang Segitiga Siku Bawah : "))
        z=" "
        for item in range(segitigasiku1):       # for dalam for (2x looping atau 2x perulangan)
            for item1 in range(0, segitigasiku1-item):
                z += " * "
            z += " \n "              #\n berfungsi sebagai enter
        print(z)
    else:
        print("Pilih Segitiga Siku Yang Ada")
elif(bentuk == "3"):
    samakaki = input("Masukkan segitiga sama kaki yang anda inginkan : 1. Segitiga Sama Kaki Atas 2. Segitiga Sama Kaki Bawah : ")
    if(samakaki == "1"):
        samakaki1 = int(input("Masukkan Panjang Segitiga Sama Kaki Atas : "))
        z=""
        for item in range(0,samakaki1,2):       # for dalam for (2x looping atau 2x perulangan)
            for item1 in range(0, samakaki1-item):
                z += " "
            for item1 in range(0, item+1):
                z += " *"
            z += "\n"              #\n berfungsi sebagai enter
        print(z) 
    elif(samakaki == "2"):
        samakaki1 = int(input("Masukkan Panjang Segitiga Sama Kaki bawah, Pilih angka Ganjil : "))
        if(samakaki1 % 2): 
            z=""
            for item in range(0,samakaki1,2):       # for dalam for (2x looping atau 2x perulangan)
                for item1 in range(0, item+1):
                    z += " "
                for item1 in range(0, samakaki1-item):
                    z += " *"
                z += "\n"              #\n berfungsi sebagai enter
            print(z) 
        else:
            print("Silahkan Masukkan Bilangan Ganjil")
    else:
        print("Pilih Segitiga Sama Kaki Yang Ada")
    
else:
    print("Pilih Yang Ada")