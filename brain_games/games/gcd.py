from random import randint

GAME_MANUAL = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    for i in range(min(num1, num2), 0, -1):
        random_digit1 = num1 % i
        random_digit2 = num2 % i
        if random_digit1 == 0 and random_digit2 == 0:
            return f'{num1} {num2}', str(i)
