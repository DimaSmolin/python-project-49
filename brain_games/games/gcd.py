from random import randint

GAME_MANUAL = 'Find the greatest common divisor of given numbers.'
NUMBER_OF_ROUNDS = 3
num1 = 0
num2 = 0


def question():
    global num1, num2
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    return f'{num1} {num2}'


def correct_answer():
    for i in range(min(num1, num2), 0, -1):
        random_digit1 = num1 % i
        random_digit2 = num2 % i
        if random_digit1 == 0 and random_digit2 == 0:
            return str(i)
