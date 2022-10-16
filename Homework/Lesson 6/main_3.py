print("№3 Задайте список из вещественных чисел.")
print("Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
print("Пример: [1.1, 1.2, 3.3, 5, 10.01] => 0.19")
# было
print("Введите дробные числа через пробел:", end=' ')
list_numbers = list(map(float, input().split()))
max_min_number = []

for i in range(len(list_numbers)):
    max_min_number.append(list_numbers[i] % 1)
difference_of_numbers = max(max_min_number) - min(max_min_number)

print(f'{(difference_of_numbers):.3}')


exit()
# стало
lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))