import time
import os


def clear(): return os.system('clear')

clear()


def show_menu():
    print('\nДобро пожаловать в базу данных учеников\n')
    time.sleep(1.5)
    print('Введите 1: добавить нового ученика в базу')
    print('Введите 2: вывести на экран всех учеников')
    print('Введите 3: найти ученика по фамилии')  # или по ФИО
    print('Введите 4: вывести на экран всех учеников определенного класса')
    print('Введите 5: завершить работу')
    choice = int(input('\nВвод: '))
    return choice
