number = int(input("Введите натуральное число: "))
list = []

for i in range(-number, number + 1):
    list.append(i)
print(list)

position_1 = int(input(f"Введите первую позицию от 0 до {number * 2}: "))
position_2 = int(input(f"Введите вторую позицию от 0 до {number * 2}: "))

product_of_numbers = (list[position_1] * list[position_2])

print(f"Произведение чисел на позициях {position_1} и {position_2} = {product_of_numbers}")