from random import randint

GAME_MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_OF_ROUNDS = 3
random_number = 0


def question():
    global random_number
    random_number = randint(2, 50)
    return random_number


def is_prime(num1):
    for i in range(2, num1 // 2):
        a = num1 % i
        if a == 0:
            return False
    return True


def correct_answer():
    if is_prime(random_number):
        return 'yes'
    else:
        return 'no'
