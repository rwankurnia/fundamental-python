# word = "Today is Sunday"

# def no_vowel(x):
#     if x not in "aiueo":
#         return True
#     else:
#         return False

# resVowel = "".join(filter(no_vowel, word))
# print(resVowel)

# ==============================================   


# angkaGenap = [2, 6, 8, 4, 7, 10, 12]
# angkaGanjil = [1, 3, 5, 7, 4, 9, 11]

# genap = []
# ganjil = []
# def outlayers(x):
#     for i in x:
#         if i % 2 == 0:
#             genap.append(i)
#         else:
#             ganjil.append(i)

#     if len(genap) > len(ganjil):
#         return ganjil
#     else:
#         return genap

# print(outlayers(angkaGanjil))

# =======================================

# inputInteger = input("Masukkan integer : ")

# def step(x):
#     if 

# ========================================

word = "Today is Sunday"
def no_vowel(x):
    j = ""
    for i in x:
        if i in "aiueo":
            del(i)
        else:
            j += i
    res = "".join(j)
    return res

resVowel = no_vowel(word)

print(resVowel)

# =====================================

# word = "Today is Friday"
# def tugasIlham(x):
#     j = ""
#     for i in x:
#         if i not in ("a", "i", "u", "e", "o"):
#             j += (i.upper() + i.lower())
#         else:
#             del(i)
#     result = "".join(j)
#     return result

# print(tugasIlham(word))

# resVowel = "".join(filter(no_vowel, word))
# print(resVowel)


