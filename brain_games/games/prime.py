from random import randint

GAME_MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    random_digit = randint(2, 50)

    if is_prime(random_digit):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return random_digit, right_answer


def is_prime(num1):
    for i in range(2, (num1 // 2) + 1):
        a = num1 % i
        if a == 0 or num1 == 1:
            return False
    if num1 == 1:
        return False
    return True
