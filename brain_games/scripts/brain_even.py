from brain_games.engine import starts_games
from brain_games.games import even


def main():
    first_questin = 'Answer "yes" if the number is even, otherwise answer "no".'
    starts_games(even, first_questin)


if __name__ == '__main__':
    main()
