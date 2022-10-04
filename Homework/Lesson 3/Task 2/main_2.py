print("Введите числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
multiplied_list = []

# добавляем в конец списка индекс i [2, 3, 4, 5] -> [2, 3, 4, 5, i] и делим список попалам
for i in range((len(list_numbers) + 1) // 2):
    # перемножаем первый и последний индекс, вычтив из последнего добавленный индекс i
    multiplied_list.append(list_numbers[i] * list_numbers[-1-i])

print(multiplied_list)