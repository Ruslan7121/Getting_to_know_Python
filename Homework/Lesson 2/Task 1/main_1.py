number = input("Введите натуральное или вещественное число: ")
sum_listof_digits = 0

for i in number:
    if i != ".":
        sum_listof_digits += int(i)
print(f"Сумма всех цифр числа {number} равна {sum_listof_digits}")