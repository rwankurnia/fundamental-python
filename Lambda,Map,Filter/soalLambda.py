words = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"]

keyword = input(f"{words} \n Search : ")

final = []

for i in words:

    res = keyword.lower() in i.lower()
    
    if res == True:
        final.append(i)

print(final) 

# print(resStrList)

# # ========================

# strList = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"]

# inputStrList = input(f"{strList} \n Search : ")

# def search(i):
#     return inputStrList.lower() in i.lower()

# result = list(filter(search, strList))

# print(result)

# # =================


# # HOMEWORK
# # Buat duplicate function untuk map dan filter

# def myMap(fun, lis):
#     # do something

# def myFilter(fun, lis):
#     # do something

#=============
# # Jawaban Bang Alvin untuk map

# numList = [2, 3, 4]

# def times2(num):
#     return num * 2

# def myMap(fun, lis):
#     mapList = []

#     for i in lis:
#         res = fun(i)
#         mapList.append(res)
#     return mapList

# myMapRes = myMap(times2, numList)
# print(numList) # Hanya untuk menampilkan List sebelom di proses
# print(myMapRes) 

#  # Jawaban Bang Alvin untuk Filter

# numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]

# def even(num):
#     return num % 2 == 0

# def myFilter(fun, lis):

#     filterList = []

#     for i in lis:

#         res = fun(i)

#         if res == True:
#             filterList.append(i)

#     return filterList
# myFilterRes = myFilter(even, numList)
# print(numList)
# print(myFilterRes)