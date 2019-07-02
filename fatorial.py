num = int(raw_input('numero:'))

fat = 1

while num != 1:
    fat = fat * num
    num -= 1
print('fatorial:' + str(fat))
