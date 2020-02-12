import math

x = 4
y = 3
z = 2

# w = (x + (y * z)) / (x * y) ** 2

# print(w)

#=================

#cara ke 2

w = (x + (y * z)) / (x * y)
w = math.pow(w, z)

print(w)
