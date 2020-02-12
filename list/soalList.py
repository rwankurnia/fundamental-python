# number = [40, 100, 1, 5, 25, 10]

# # number.sort()
# # print(f"Tertinggi adalah {number[5]} dan terendah adalah {number[0]}")

# min = number[0]
# max = number[0]

# def minMax(listNumber):
#     for i in listNumber:
#         if i == min:
#             number.sort()
#         else:
#             number.sort(reverse=True)

# # print(f"Tertinggi adalah {max} dan terendah adalah {min}")
# print(minMax)



x = [40, 100, 1, 5, 25, 10]
min = x[0]
max = x[0]
for i in range(len(x)):
    if max < x[i]:
        max = x[i]
    if min > x[i]:
        min = x[i]

print("Elemen Tertinggi adalah :", max)
print("Elemen Terendah adalah :", min)