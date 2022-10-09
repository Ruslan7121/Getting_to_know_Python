print("Введите список чисел через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
result = []

for i in range(0, len(list_numbers)):
    count = 0
    for j in range(0, len(list_numbers)):
        if i != j:
            if list_numbers[i] == list_numbers[j]:
                count = 1
    if count == 0:
        result.append(list_numbers[i])

print(f"Cписок неповторяющихся элементов исходной последовательности {result}")