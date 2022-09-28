from brain_games.engine import starts_games
from brain_games.games import progression


def main():
    first_questin = 'What number is missing in the progression?'
    starts_games(progression, first_questin)


if __name__ == '__main__':
    main()
