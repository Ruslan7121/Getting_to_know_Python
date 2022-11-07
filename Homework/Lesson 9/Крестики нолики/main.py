from time import sleep
import os
def clear(): return os.system('cls')
import emoji 

clear()
print("⊹──⊱ Игра \"Крестики-нолики\" ⊰──⊹\n")
sleep(2.5)
print("Загрузка... ████████████] 99%")
sleep(2.5)
clear()


board = list(range(1, 10))

# заполняет поле построчно
def draw_board(board):
    print("-" * 13)  # первая горизонтальная линия
    for i in range(3):  # проходим по трем строчкам
        # с каждым проходом строчки мы выводим число из списка по порядку по три столбика по позициям чисел в списке
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        # выводит линию после каждого прохода по строчке, т.е. три линии
        print("-" * 13)

# заполнение ячеек в поле
def take_input(player_token):
    valid = False
    while not valid:  # цикл заполнения если нет ошибки
        # спрашиевает в зависимости от игрока ставить Х или О
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            # принимает на вход число в клетке поля куда поставить Х или О
            player_answer = int(player_answer)
        except:
            # проверка на ввод целого числа, а не символа или натурального числа
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        # если введено целое число, то проверка на ввод числа от 1 до 9
        if player_answer >= 1 and player_answer <= 9:
            # проверка не заполнена ли клетка Х или О
            if (str(board[player_answer -1]) not in "XO"): # если в поле не Х или О, то в список на позицию числа (число - 1) ставится Х или О
                board[player_answer-1] = player_token
                valid = True  # для проверки на правильность ввода
            else:
                print("Эта клетка уже занята!")  # выводит если всё верно
        else:
            # выводит если ошибка в вводе
            print("Некорректный ввод. Введите число от 1 до 9.")
    clear()


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # кортеж со всеми выйгрышными комбинациями
    for each in win_coord:  # перебор кортежа
        # если символы во всех трех заданных клетках равны - возвращаем выигрышный символ, иначе - возвращаем значение False
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]  # если верно
    return False  # если неверно


def main(board):  # компилятор игры
    counter = 0  # счетчик
    win = False
    while not win:  # цикл до победы
        draw_board(board)  # вызов игрового поля
        if counter % 2 == 0:  # передача хода от игрока к игроку до строки 47
            take_input(emoji.emojize(":lemon:"))
        else:
            take_input(emoji.emojize(":green_apple:"))
        counter += 1
        if counter > 4:  # до 4 ходов никто выйграть не может, после этого проверка на выйгрыш
            tmp = check_win(board) # вызов метода проверки выйгрышных комбинаций
            if tmp:  # условие вывода выйгрыша
                print('{color} {} {endcolor}'.format(f"{tmp} выиграл\n", color='\x1b[1;32m', endcolor='\x1b[0m'))
                win = True  # для остановки цикла while
                break
        if counter == 9:  # если полностью закрыты все клетки, и нет победтеля то выводит "Ничья!""
            print('{color} {} {endcolor}'.format("Ничья!\n", color='\x1b[1;31m', endcolor='\x1b[0m'))
            break
    draw_board(board)

main(board)  # вызов компилятора
input("Нажмите Enter для выхода!")  # остановка программы