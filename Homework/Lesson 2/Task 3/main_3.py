number = int(input("Введите натуральное число: "))
list = []
sum_list = 0

for i in range(1, number + 1):
    list.append((1 + 1 / i) ** i)

for number in list:
    sum_list += number
print(f'{sum_list:.5}')