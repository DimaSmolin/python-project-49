from brain_games.engine import starts_games
from brain_games.games import gcd


def main():
    first_questin = 'Find the greatest common divisor of given numbers.'
    starts_games(gcd, first_questin)


if __name__ == '__main__':
    main()
