from random import randint


def prime_dig():
    num1 = randint(2, 50)
    count = 0
    print('Question:', num1)
    for i in range(2, num1):
        a = num1 % i
        if a == 0:
            count += 1
    if count == 0:
        return 'yes'
    else:
        return 'no'


def answr_prm():
    return input('Your answer:')
