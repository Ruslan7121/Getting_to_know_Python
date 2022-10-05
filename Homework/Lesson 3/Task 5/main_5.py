number = int(input("Введите число: "))
list_fibonacci  = [0, 1]

for i in range(2, number + 1):
    list_fibonacci.append(list_fibonacci[i-1] + list_fibonacci[i-2])

for i in range(number):
    list_fibonacci.insert(0, list_fibonacci[1] - list_fibonacci[0])

print(f"Для k = {number} список чисел Фибоначчи: {list_fibonacci}")