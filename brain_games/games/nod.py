from random import randint


def rand_digit():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print('Question:', num1, num2) # исправлено

    for i in range(max(num1, num2), 0, -1):
        a = num1 % i
        b = num2 % i
        if a == 0 and b == 0 and a == b:
            return i


def gm_ans():
    return int(input('Your answer:'))
