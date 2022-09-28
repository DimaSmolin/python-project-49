from brain_games.engine import starts_games
from brain_games.games import prime


def main():
    first_ques = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    starts_games(prime, first_ques)


if __name__ == '__main__':
    main()
