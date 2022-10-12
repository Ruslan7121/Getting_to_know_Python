from time import sleep
import random
import os
def clear(): return os.system('cls')


clear()
cand = int(input("Введите количество конфет: "))
max_cand = int(input(
    "\nВведите максимальное количество конфет, которые можно забрать за один ход: "))
draw = random.choice(["Бот", "Вы"])
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


def bot(candy, max_candy):
    while candy != 0:
        print(f"На столе лежат {candy} конфет\n")
        sleep(1.5)
        if candy < max_candy:
            max_candy = candy
        bot = random.randint(1, max_candy)
        candy -= bot
        print(f"Бот забрал {bot} конфет, осталось {candy}")
        sleep(1.5)
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print('{color} {} {endcolor}'.format(
                "Вы выиграли!", color='\x1b[1;32m', endcolor='\x1b[0m'))
            break

        else:
            number = check_num(max_candy)
            candy -= number
            print(f"Вы забрали {number} конфет, осталось {candy}")
            sleep(2)
            clear()
            if candy == 0:
                print('{color} {} {endcolor}'.format(
                    "Вы проиграли!", color='\x1b[1;31m', endcolor='\x1b[0m'))
                break
            else:
                continue


def person(candy, max_candy):
    while candy != 0:
        print(f"На столе лежат {candy} конфет\n")
        sleep(1.5)
        if candy < max_candy:
            max_candy = candy
        number = check_num(max_candy)
        candy -= number
        print(f"Вы забрали {number} конфет, осталось {candy}\n")
        sleep(2)
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print('{color} {} {endcolor}'.format(
                "Вы проиграли!", color='\x1b[1;31m', endcolor='\x1b[0m'))
            break

        else:
            bot = random.randint(1, max_candy + 1)
            candy -= bot
            print(f"Бот забрал {bot} конфет, осталось {candy}")
            sleep(2)
            clear()
            if candy == 0:
                print('{color} {} {endcolor}'.format(
                    "Вы выиграли!", color='\x1b[1;32m', endcolor='\x1b[0m'))
                break
            else:
                continue

if draw == 'Бот':
    bot(cand, max_cand)
else:
    person(cand, max_cand)