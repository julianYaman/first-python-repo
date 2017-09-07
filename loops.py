# FOR LOOPS

# names = ["Julian", "Johannes", "Fabian", "Kevin", "Marius"]
#
# for name in names:
#     print(name)

age = 25
num = 0

# WHILE LOOP

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num +=1
