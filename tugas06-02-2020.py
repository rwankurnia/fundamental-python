## Home Work
# if else:

# Jika sebuah kata diawali dengan huruf vokal "a, i, u, e, o", tambahkan huruf ay
# Jika tidak, taruh huruf pertama di paling beakang kemudian tambahkan ay

## Pake Return

inputText = input("Masukkan kata : ")

def changeWorld(text):
    if text[0] in ["a", "i", "u", "e", "o"]:
        text = text + "ay"
    else:
        text = text[1:] + text[0] + "ay"
    return text
print(changeWorld(inputText))

## ======================
## Tidak Pake Return

# inputText = input("Masukkan kata : ")

# def changeWorld(text):
#     if text[0] in ["a", "i", "u", "e", "o"]:
#         text = text + "ay"
#     else:
#         text = text[1:] + text[0] + "ay"
#     print(text)
# (changeWorld(inputText))