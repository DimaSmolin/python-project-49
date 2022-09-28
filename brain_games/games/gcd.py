from random import randint


def question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print('Question:', num1, num2)

    for i in range(min(num1, num2), 0, -1):
        random_digit1 = num1 % i
        random_digit2 = num2 % i
        if random_digit1 == 0 and random_digit2 == 0:
            return str(i)
