from random import randint

GAME_MANUAL = 'Answer "yes" if number even otherwise answer "no".'
NUMBER_OF_ROUNDS = 3
random_number = 0


def question():
    global random_number
    random_number = randint(1, 100)
    return random_number


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def correct_answer():
    if is_even(random_number):
        return 'yes'
    else:
        return 'no'
