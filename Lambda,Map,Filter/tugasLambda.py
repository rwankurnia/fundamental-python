# for in
# if else
# len
# join
# print


employee = [
    {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
    {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
    {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
]

# Mr. Steve has 2 hobbies, they are Video games, Football

# Mrs. Lina has 2 hobbies, they are Shop, Cook

# Mr. Reynald has 3 hobbies, they are Run, Hide, Jump

# Setiap loop:
#   jika gender == male
#           nama = Mr. + nama
#   else
#           nama = Mrs. + nama


for i in employee:
    # i = {"name", "gender", "hobbies"}
    # Jika gendernya adalah laki laki, tambahkan kata Mr.
    # Jika bukan, tambahkan kata Mrs.
    if i["gender"] == 'male':
        i["name"] = 'Mr.' + i["name"]
    else :
        i["name"] = 'Mrs.' + i["name"]

    name = i["name"]
    # Menggabungkan semua data pada list menggunakan ", "
    hobbies = ", ".join(i["hobbies"])
    # Mencari tahu jumlah hobby yang dimiliki
    lenHob = len(i["hobbies"])

    print(
        f'{name} has {lenHob} hobbies, they are {hobbies}'
    )