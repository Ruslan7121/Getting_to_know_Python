print("Введите список чисел через пробел:", end=' ')
numbers = list(map(int, input().split()))
numbers.sort
print(f"Самое большое число {numbers[-1]} самое маленькое число {numbers[0]}")