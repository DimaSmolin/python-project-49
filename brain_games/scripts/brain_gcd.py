from brain_games.games.dvij_2 import general_logics
from brain_games.games.nod import gm_ans, rand_digit


def main():
    first_questin = 'Find the greatest common divisor of given numbers.'
    general_logics(gm_ans, rand_digit, first_questin)


if __name__ == '__main__':
    main()
