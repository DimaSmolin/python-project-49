import operator
from random import randint, choice

GAME_MANUAL = 'What is the result of the expression?'


def question_and_answer():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    symbl = '+-*'
    char = choice(symbl)

    correct_answer = 0
    if '+' == char:
        correct_answer = operator.add(random_num1, random_num2)
    elif '-' == char:
        correct_answer = operator.sub(random_num1, random_num2)
    elif '*' == char:
        correct_answer = operator.mul(random_num1, random_num2)

    return f'{random_num1} {char} {random_num2}', str(correct_answer)
