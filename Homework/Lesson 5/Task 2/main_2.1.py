from time import sleep
import random
import os
def clear(): return os.system('cls')


clear()
print('Договоритесь между собой кто будет "Игрок I", а кто "Игрок II"')
cand = int(input("\nВведите количество конфет: "))
max_cand = int(input(
    "\nВведите максимальное количество конфет, которые можно забрать за один ход: "))
draw = random.choice(["Игрок I", "Игрок II"])
print(f'\nПервым ходит: {draw}')
sleep(2.5)
clear()


def check_num(max_can):
    x = int(
        input(f"Вы можете забрать конфеты в диапозоне от {1} - {max_can}: "))
    while x < 1 or x > max_can:
        x = int(
            input(f"Вы можете забрать конфеты в диапозоне от {1} - {max_can}: "))
    return x


def person_1(candy, max_candy):
    while candy != 0:
        print(f"На столе лежат {candy} конфет\n")
        sleep(1.5)
        if candy < max_candy:
            max_candy = candy
        number = check_num(max_candy)
        candy -= number
        print(f"Игрок I забрал {number} конфет, осталось {candy}\n")
        sleep(2)
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print('{color} {} {endcolor}'.format("Игрок II выиграл!", color='\x1b[1;33m', endcolor='\x1b[0m'))
            break

        else:
            number = check_num(max_candy)
            candy -= number
            print(f"Игрок II забрал {number} конфет, осталось {candy}")
            sleep(2)
            clear()
            if candy == 0:
                print('{color} {} {endcolor}'.format("Игрок I выиграл!", color='\x1b[1;34m', endcolor='\x1b[0m'))
                break
            else:
                continue


def person_2(candy, max_candy):
    while candy != 0:
        print(f"На столе лежат {candy} конфет\n")
        sleep(1.5)
        if candy < max_candy:
            max_candy = candy
        number = check_num(max_candy)
        candy -= number
        print(f"Игрок II забрал {number} конфет, осталось {candy}\n")
        sleep(2)
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print('{color} {} {endcolor}'.format("Игрок I выиграл!", color='\x1b[1;34m', endcolor='\x1b[0m'))
            break

        else:
            number = check_num(max_candy)
            candy -= number
            print(f"Игрок I забрал {number} конфет, осталось {candy}")
            sleep(2)
            clear()
            if candy == 0:
                print('{color} {} {endcolor}'.format("Игрок II выиграл!", color='\x1b[1;33m', endcolor='\x1b[0m'))
                break
            else:
                continue


if draw == 'Игрок I':
    person_1(cand, max_cand)
else:
    person_2(cand, max_cand)