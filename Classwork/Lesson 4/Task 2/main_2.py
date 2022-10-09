print("Введите значения A, B и C через пробел:", end=' ')
a, b, c = list(map(int, input().split()))

if a != 0 and (b**2 - 4 * a * c) >= 0:
    x1 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    print({x1, x2})
else:
    print("Корней нет!")