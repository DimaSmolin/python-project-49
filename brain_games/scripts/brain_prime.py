from brain_games.games.dvij_2 import general_logics
from brain_games.games.prime import answr_prm, prime_dig


def main():
    first_ques = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    general_logics(answr_prm, prime_dig, first_ques)


if __name__ == '__main__':
    main()
