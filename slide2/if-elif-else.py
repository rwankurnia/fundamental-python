umur = input("Masukkan Umur Kamu : ")
umur = int(umur)

if (umur >= 18) :
    print("Boleh Masuk")
elif (umur >= 15 and umur < 18) :
    print("Boleh Masuk dengan orang tua")
else:
    print("Tidak Boleh Masuk")