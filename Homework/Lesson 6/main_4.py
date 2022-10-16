print("№4 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов")
print("Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]")
# было
number = int(input("Введите число: "))
list_fibonacci  = [0, 1]

for i in range(2, number + 1):
    list_fibonacci.append(list_fibonacci[i-1] + list_fibonacci[i-2])
for i in range(number):
    list_fibonacci.insert(0, list_fibonacci[1] - list_fibonacci[0])

print(f"Для k = {number} список чисел Фибоначчи: {list_fibonacci}")


exit()
# стало
number = int(input('Введите число k: '))
x = [0,1]
list_fibonacci = x[0:2] + [x.append(x[-1] + x[-2]) or x[-1] for i in range(number-2)]
print(list_fibonacci)