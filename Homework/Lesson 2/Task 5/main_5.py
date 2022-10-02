import time

print("Заполните список из натуральных чисел через пробел и нажмите Enter:", end=' ')
time_string = str(time.time_ns())
list = list(map(int, input().split()))
print(f"Список ваших значений: {list}")
print("\nНаглядный процесс перемешивания:")

for i in range(0, len(list)):
    for j in time_string:
        if int(j) < len(list):
            list[i], list[int(j)] = list[int(j)], list[i]   
    print(list)

print(f"\nПеремешанный список: {list}")