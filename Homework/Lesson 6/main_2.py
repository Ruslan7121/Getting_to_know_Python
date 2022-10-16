print("№2 Напишите программу, которая найдёт произведение пар чисел списка.")
print("Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
print("Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]")
# было
print("Введите числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
multiplied_list = []

# добавляем в конец списка индекс i [2, 3, 4, 5] -> [2, 3, 4, 5, i] и делим список попалам
for i in range((len(list_numbers) + 1) // 2):
    # перемножаем первый и последний индекс, вычтив из последнего добавленный индекс i
    multiplied_list.append(list_numbers[i] * list_numbers[-1-i])

print(multiplied_list)

exit()
# стало
def multiplied_list(list_numbers):
    l = len(list_numbers)//2 + 1 if len(list_numbers) % 2 != 0 else len(list_numbers)//2
    new_list_numbers = [list_numbers[i]*list_numbers[len(list_numbers)-i-1] for i in range(l)]
    print(new_list_numbers)

print("Введите числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
multiplied_list(list_numbers)