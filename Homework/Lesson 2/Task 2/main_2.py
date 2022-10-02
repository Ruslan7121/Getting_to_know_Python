number = int(input("Введите натуральное число: "))
list = []
count = 1

for i in range(1, number + 1):
    list.append(count)
    count *= i + 1
print(list)