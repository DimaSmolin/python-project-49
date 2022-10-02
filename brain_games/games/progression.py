from random import randint

GAME_MANUAL = 'What number is missing in the progression?'
NUMBER_OF_ROUNDS = 3
correct_answer_var = 0


def question():
    empty_list = []
    global correct_answer_var

    start_num = randint(1, 9)
    step_num = randint(2, 5)

    for i in range(10):
        empty_list.append(start_num)
        start_num += step_num

    secret_num = randint(0, len(empty_list) - 1)
    correct_answer_var = empty_list[secret_num]
    empty_list[secret_num] = '..'

    empty_string = ''
    for k in range(len(empty_list)):
        empty_string += f'{empty_list[k]} '

    return empty_string


def correct_answer():
    return str(correct_answer_var)
