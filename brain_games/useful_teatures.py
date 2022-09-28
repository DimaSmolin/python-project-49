def parity_check_function(num):
    num = num
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def checking_for_simplicity(num1):
    for i in range(2, num1):
        a = num1 % i
        if a == 0:
            return 'no'
    return 'yes'
