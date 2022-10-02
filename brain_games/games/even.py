from random import randint

GAME_MANUAL = 'Answer "yes" if number even otherwise answer "no".'


def question_and_answer():
    random_number = randint(1, 100)

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return random_number, correct_answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
