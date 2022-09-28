from brain_games.engine import starts_games
from brain_games.games import calc


def main():
    starts_games(calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
