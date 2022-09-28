from random import randint


def question():
    empty_list = []

    start_num = randint(1, 9)
    step_num = randint(2, 5)
    for i in range(10):
        empty_list.append(start_num)
        start_num += step_num

    secret_num = randint(0, len(empty_list) - 1)
    char = empty_list[secret_num]

    index_num = empty_list.index(char)
    empty_list[index_num] = '..'

    print('Question:', *empty_list)
    return str(char)
