num = int(input('Введите число N: '))
list = []
for i in range(num):
    elem = 3 * (i + 1) + 1
    list.append(elem)
print(list)