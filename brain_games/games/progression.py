from random import randint

GAME_MANUAL = 'What number is missing in the progression?'


def question_and_answer():
    empty_list = []
    start_num = randint(1, 9)
    step_num = randint(2, 5)

    for i in range(10):
        empty_list.append(start_num)
        start_num += step_num

    secret_num = randint(0, len(empty_list) - 1)
    correct_answer = empty_list[secret_num]
    empty_list[secret_num] = '..'

    empty_string = ''
    for k in range(len(empty_list)):
        empty_string += f'{empty_list[k]} '

    return empty_string, str(correct_answer)
