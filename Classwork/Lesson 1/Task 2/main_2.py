array = []
for i in range(5):
    array.append(int(input(f'Введите {i + 1} число: ')))
print(input(f'Максимальное число: {max(array)}'))