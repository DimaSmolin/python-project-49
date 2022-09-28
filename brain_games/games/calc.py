import operator
from random import randint, choice


def question():
    digit_1 = randint(1, 100)
    digit_2 = randint(1, 100)
    symbl = '+-*'
    char = choice(symbl)
    random_math = f'{digit_1} {char} {digit_2}'
    print('Question:', random_math)

    corr_answer = 0
    if char == '+':
        corr_answer = operator.add(digit_1, digit_2)
    elif char == '-':
        corr_answer = operator.sub(digit_1, digit_2)
    elif char == '*':
        corr_answer = operator.mul(digit_1, digit_2)
    return str(corr_answer)
