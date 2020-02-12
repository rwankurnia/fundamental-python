## Reversed Sentence = Untuk Membalik List
## Hello my friend --> friend my hello
## This is friday  --> friday is this

## split()
## reverse()
## join

# inputText = input("Masukkan kata : ")

# def sentRev(text):
#     wordAgain = text.split(" ")
#     wordAgain.reverse()
#     text = " ".join(wordAgain)

#     return text

# print(sentRev(inputText))

##======================================================
## CARA KE 2

# inputText = input("Masukkan kata : ")

# def sentRev(text):
#     wordAgain = text.split(" ")
#     wordAgain.reverse()
#     text = " ".join(wordAgain)

#     print(text)

# sentRev(inputText)

##==============================
## Soal mencari apakah 9 berdekatan

## CARA KE 1

# def has99(lis):
#     idx = lis.index(9)
#     if lis[idx + 1] == 9:
#         return True
#     else:
#         return False

# print(has99([1, 9, 9]))
# print(has99([5, 9, 2, 9]))
# print(has99([9, 3, 9]))
# print(has99([7, 9, 9, 6]))

##===============================
## CARA KE 2

# def has99(lis):
#     idx = lis.index(9)
#     return lis[idx + 1] == 9

# print(has99([1, 9, 9]))
# print(has99([5, 9, 2, 9]))
# print(has99([9, 3, 9]))
# print(has99([7, 9, 9, 6]))

##==================================
### SOAL ####

## Number One
## def wordRev
## Buatlah sebuah function yang menerima sebuah kata
## Reverse huruf setiap kata

## Contoh:
## Hello my friend --> olleH ym dneirf
## abc de efg  --> cba ed gfe


# inputText = input("Masukkan kata : ")

# def sentRev(text):
#     wordAgain = text.split(" ")
#     wordAgain.reverse()
#     text = " ".join(wordAgain)

#     return text
# print(sentRev(inputText))

## Number Two
## def sum01
## Buat function yang menerima list of number
## Jumlahkan semua angka, kecuali angka yang ada diantara angka 0 - 1

## [2, 4, 0, 1, 11] --> 17      (0, 1 tidak masuk hitungan)
## [7, 0, 3, 1, 7, 9] --> 23    (0, 3, 1 tidak masuk hitungan)
## [5, 0, 3, 2, 1] --> 5        (0, 3, 2, 1 tidak masuk hitungan)      
    
def sum01(lis):
    # Temukan index angka 0 dan 1
    # Untuk index angka 1 dijumlahkan dengan angka
    zero = lis.index(0)
    one = lis.index(1) + 1

    del lis[zero:one]

    result = sum(lis)

    print(result)

sum01([5, 0, 3, 1, 2, 1])


