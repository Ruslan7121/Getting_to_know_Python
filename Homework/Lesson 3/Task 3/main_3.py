print("Введите дробные числа через пробел:", end=' ')
list_numbers = list(map(float, input().split()))
max_min_number = []

for i in range(len(list_numbers)):
    max_min_number.append(list_numbers[i] % 1)
difference_of_numbers = max(max_min_number) - min(max_min_number)

print(f'{(difference_of_numbers):.3}')