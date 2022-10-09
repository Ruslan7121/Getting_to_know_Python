# Создание первого файла с многочленом
text1 = open('file_1.txt', 'w', encoding="utf-8") 
text1.write('3x² + 14x + 16 = 0')
text1.close()

# Создание второго файла с многочленом
text2 = open('file_2.txt', 'w', encoding="utf-8") 
text2.write('3x² + 6x + 1 = 0')
text2.close()

# Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
text_1 = open('file_1.txt', 'r') 
line1 = text_1.read().split('+')
line1 = [i.lstrip() for i in line1]
text1.close()

# Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
text_2 = open('file_2.txt', 'r') 
line2 = text_2.read().split('+')
line2 = [i.lstrip() for i in line2]
text2.close()

line1 = [int(i[0]) for i in line1]
line2 = [int(i[0]) for i in line2]
line3 = []
for i in range(3): # Суммирование коэффициентов многочлена
    line3.append(line1[i] + line2[i]) 

# Создание окончательного текста многочлена
list = str(line3[0]) + 'x²' + '+' + str(line3[1]) + '+' + str(line3[2])  + '=0' 

# Запись полученного текста в файл
text3 = open('file_3.txt', 'w', encoding="utf-8") 
text3.write(list)
text3.close()