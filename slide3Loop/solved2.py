        # solve it
# z = " "
# i = 0 
# while(i <= 4):
#     z += "* "
#     print(z)
#     i += 1

#============================
        #solved segitiga siku2
# z=" "
# for item in range(5):       
#     for item1 in range(item+1):
#         z += " * "
#     z += " \n "              
# print(z)          

#==========================
    #Cara pak ALvin
# stars = ''
# row = 5

# # Banyaknya baris
# for i in range(row):
#     # Banyaknya bintang per baris
#     for j in range(i + 1):
#         stars += ' * '

#     stars += '\n'

# print(stars)

#===========================
        #Solve it! 1 segitiga siku2 terbalik
# stars =" "
# for i in range(5):       
#     for j in range(5-i):
#         stars += " * "
#     stars += " \n "              
# print(stars)

#============================
    #cara bang Alvin

# stars =" "
# for i in range(5):       
#     for j in range(5, i, -1):
#         stars += " * "
#     stars += " \n "              
# print(stars)

#===========================
        #Solve it double mirror 2 segitiga siku2
# z=" "
# for item in range(9):       # for dalam for (2x looping atau 2x perulangan)
#     if item in range(5):
#         # print(item,"q") #justcheck
#         for item1 in range(5,item, -1):
#             z += " * "
#         z += " \n "              #\n berfungsi sebagai enter
#     else:
#         # print(item) #justcheck
#         for item1 in range(4, item+1):
#             z += " * "
#         z += " \n "
# print(z) 

#================================
    #Cara Bang Alvin

# stars=" "
# for i in range(9):       # for dalam for (2x looping atau 2x perulangan)
#     if i in range(5):
#         # print(item,"q") #justcheck
#         for j in range(5,i,-1):
#             stars += " * "
#         stars += " \n "              #\n berfungsi sebagai enter
#     else:
#         # print(item) #justcheck
#         for j in range(4, i+1):
#             stars += " * "
#         stars += " \n "
# print(stars) 

#===============================
        #solve it 3
# z=""
# for item in range(0,18,2):       # for dalam for (2x looping atau 2x perulangan)
#     for item1 in range(0, 18-item):
#         z += " "
#     for item1 in range(0, item+1):
#         z += " *"
#     z += "\n"              #\n berfungsi sebagai enter
# print(z) 

#================================
        #solve it 4
# z=""
# for item in range(0,19,2):       # for dalam for (2x looping atau 2x perulangan)
#     for item1 in range(0, item+1):
#         z += " "
#     for item1 in range(0, 19-item):
#         z += " *"
#     z += "\n"              #\n berfungsi sebagai enter
# print(z) 

#================================
        #solve it 5
# z=""
# for item in range(0,19,2):      # for dalam for (2x looping atau 2x perulangan)
#     if item in range(9):
#         # print(item)
#         for item1 in range(0, 9-item):
#             z += " "
#         for item1 in range(0, item+1):
#             z += "* "
#         z += "\n"              #\n berfungsi sebagai enter
#     else:
#         for item1 in range(11, item+1):
#             z += " "
#         for item1 in range(0, 19-item):
#             z += " *"
#         z += "\n"         
# print(z) 
