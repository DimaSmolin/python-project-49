import operator
from random import randint, choice

GAME_MANUAL = 'What is the result of the expression?'
NUMBER_OF_ROUNDS = 3
random_num1 = 0
random_num2 = 0
char = ''


def question():
    global random_num1, random_num2, char
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    symbl = '+-*'
    char = choice(symbl)
    return f'{random_num1} {char} {random_num2}'


def correct_answer():
    correct_answer_var = 0
    if '+' == char:
        correct_answer_var = operator.add(random_num1, random_num2)
    elif '-' == char:
        correct_answer_var = operator.sub(random_num1, random_num2)
    elif '*' == char:
        correct_answer_var = operator.mul(random_num1, random_num2)
    return str(correct_answer_var)
