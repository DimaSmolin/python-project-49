from brain_games.game import general_logics
from brain_games.games.even import answr_prm, question_correct_even


def main():
    first_questin = 'Answer "yes" if the number is even, otherwise answer "no".'
    general_logics(answr_prm, question_correct_even, first_questin)


if __name__ == '__main__':
    main()
