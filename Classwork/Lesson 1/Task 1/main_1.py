a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a**2 == b or b**2 == a:
    print('Да. Одно число является квадратом другого')
else:
    print('Нет. Одно число не является квадратом другого')