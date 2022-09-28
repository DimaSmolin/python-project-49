from random import randint

from brain_games.useful_teatures import checking_for_simplicity


def question():
    num1 = randint(2, 50)
    print('Question:', num1)
    return checking_for_simplicity(num1)
