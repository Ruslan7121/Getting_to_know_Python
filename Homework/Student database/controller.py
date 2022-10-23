from modul import *
from view import show_menu


def Menu(stud_base):
    choice = show_menu()
    while (choice != 0):
        if choice == 1:
            Import(stud_base)
            choice = 0
        if choice == 2:
            PrintDataBase(stud_base)
            choice = 0
        if choice == 3:
            FindStudent(stud_base)
            choice = 0
        if choice == 4:
            PrintClass(stud_base)
            choice = 0 