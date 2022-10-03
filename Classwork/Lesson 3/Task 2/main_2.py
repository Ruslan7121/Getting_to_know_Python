list_of_values = ["123", "234", "123", "567", "were", "33", "324", "www"]
value = 324

for i in range(len(list_of_values)):
    if type(list_of_values[i]) == int:
        if list_of_values[i] == value:
            print(f"Нашли заданное: {i}")
            break
    elif type(list_of_values[i]) == str:
        if list_of_values[i].isdigit() and int(list_of_values[i]) == value:
            print(f"Нашли заданное значение {value} на {i} позиции")
            break
else:
    print(f"Заданное значение {value} не найдено")