import random

def polynomial(natural_degree):
    summ = ""
    member_of_polynomial = 0

    for i in range(natural_degree, 0, -1):
        member_of_polynomial = random.randint(0, 100)
        if member_of_polynomial == 0:
            summ += ""
        elif member_of_polynomial == 1:
            summ += str(f"x^{i} + ")
        elif i != 1:
            summ += str(f"{member_of_polynomial}x^{i} + ")
        else:
            summ += str(f"{member_of_polynomial}x ")
    member_of_polynomial = random.randint(0, 100)
    if member_of_polynomial != 0:
        summ += str(f"+ {member_of_polynomial} = 0")
    else:
        summ += str(f"= 0")
    return summ

natural_degree = int(input("Введите степень больше 0: "))
print(polynomial(natural_degree))