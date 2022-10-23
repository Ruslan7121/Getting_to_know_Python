import csv


def Import(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    try:
        lastID = str(int(reader[-1][0]) + 1)
    except IndexError:
        lastID = '1'
    contacts.close()
    contacts = open(file, 'a', encoding='utf-8')
    second_name = input('\nВведите фамилию ученика: ')
    first_name = input('Введите имя ученика: ')
    patronymic = input('Введите отчетство ученика: ')
    birth_date = input('Введите дату рождения ученика: ')
    class_num = input('Введите класс ученика: ')
    class_liter = input('Введите литеру класса: ')
    contacts.writelines(lastID + ',' + second_name + ',' + first_name + ',' +
                        patronymic + ',' + class_num + ',' + class_liter + ',' + birth_date + '\n')
    contacts.close()
    print('\nДобавление успешно')


def PrintDataBase(file):
    contacts = open(file, 'r', encoding='utf-8')
    for line in contacts:
        print()
        print(line.replace(',', '  '))
    contacts.close()
    print('\nКонец базы учеников')


def FindStudent(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    second_name = input('\nВведите фамилию ученика: ')
    # first_name = input('Введите имя ученика: ')
    # patronymic = input('Введите отчество ученика: ')
    flag = False
    for i in range(1, len(reader)):
        # if second_name in reader[i] and first_name in reader[i] and patronymic in reader[i]:
        if second_name in reader[i]:
            if not flag:
                print()
                print(' | '.join(reader[i]))
    if flag:
        print('\nУченик не найден')
    contacts.close()


def PrintClass(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    class_num = input('\nВведите номер класса: ')
    class_liter = input('Введите литеру класса: ')
    flag = False
    for i in range(1, len(reader)):
        if class_num in reader[i] and class_liter in reader[i]:
            if not flag:
                print()
                print(' | '.join(reader[i]))
    if flag:
        print('\nУченики не найдены')
    contacts.close()