from brain_games.games.dvij_2 import general_logics
from brain_games.games.progression import gm_answr, quest_corr


def main():
    first_questin = 'What number is missing in the progression?'
    general_logics(gm_answr, quest_corr, first_questin)


if __name__ == '__main__':
    main()
