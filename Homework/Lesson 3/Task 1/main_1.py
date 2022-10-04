print("Введите целые числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
sum = 0

for i in range(len(list_numbers)):
    if i % 2 != 0:
        sum = sum + list_numbers[i]

print(f"Сумма чисел, стоящих на нечётных позицииях = {sum}")