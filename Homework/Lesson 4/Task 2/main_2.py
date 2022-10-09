number = int(input("Задайте натуральное число: "))
result = []
first_prime_number = 2

while first_prime_number != number:
        if number % first_prime_number == 0:
            number /= first_prime_number
            result.append(first_prime_number)
        else:
            first_prime_number += 1
else:
    result.append(first_prime_number)

print(result)