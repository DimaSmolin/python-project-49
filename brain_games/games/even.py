from random import randint

from brain_games import useful_teatures


def question():
    num = randint(1, 100)
    print('Question:', num)
    return useful_teatures.parity_check_function(num)
