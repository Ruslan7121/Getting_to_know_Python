quarter_number = int(input('Введить номер четверти системы координат: '))

if quarter_number == 1:
    print('В четверти', quarter_number, 'находятся значения X от 0 и до +∞ и значения Y от 0 и до +∞')
elif quarter_number == 2:
    print('В четверти', quarter_number, 'находятся значения X от 0 и до -∞ и значения Y от 0 и до +∞')
elif quarter_number == 3:
    print('В четверти', quarter_number, 'находятся значения X от 0 и до -∞ и значения Y от 0 и до -∞')
elif quarter_number == 4:
    print('В четверти', quarter_number, 'находятся значения X от 0 и до +∞ и значения Y от 0 и до -∞')
else:
    print('Такой четверти нет')