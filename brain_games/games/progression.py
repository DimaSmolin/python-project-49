from random import randint


def quest_corr():
    my_list = []

    start_num = randint(1, 9)
    step_num = randint(2, 5)
    for i in range(10):
        my_list.append(start_num)
        start_num += step_num

    secret_num = randint(0, len(my_list) - 1)
    char = my_list[secret_num]

    index_num = my_list.index(char)
    my_list[index_num] = '..'

    print('Question:', *my_list)
    return char


def gm_answr():
    return int(input('Your answer:'))
