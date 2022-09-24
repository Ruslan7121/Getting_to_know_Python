x_1 = int(input('Введите X координату I точки: '))
y_1 = int(input('Введите Y координату I точки: '))
x_2 = int(input('Введите X координату II точки: '))
y_2 = int(input('Введите Y координату II точки: '))

if x_1 < 0:
    x_1 = x_1 * -1
else:
    x_1

if x_2 < 0:
    x_2 = x_2 * -1
else:
    x_2

if y_1 < 0:
    y_1 = y_1 * -1
else:
    y_1

if y_2 < 0:
    y_2 = y_2 * -1
else:
    y_2

x = (x_1 + x_2) ** 2
y = (y_1 + y_2) ** 2

square_of_the_hypotenuse = round((x + y) ** (0.5), 2)
print(square_of_the_hypotenuse)