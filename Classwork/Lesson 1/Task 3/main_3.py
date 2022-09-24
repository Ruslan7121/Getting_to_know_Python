a = int(input('Введите число: '))

for i in range(2, a):
    while a % i == 0:
        print(i, end=' ')
        a //= i