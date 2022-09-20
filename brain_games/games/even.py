from random import randint


def question_correct_even():
    num = randint(1, 100)
    print('Question:', num)
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def answr_prm():
    return input('Your answer:')
