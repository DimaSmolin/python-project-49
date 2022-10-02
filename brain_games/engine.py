import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_MANUAL)

    count = 0
    for i in range(game.NUMBER_OF_ROUNDS):
        question = game.question()
        print('Question:', str(question))
        corrct = game.correct_answer()
        answ = prompt.string('Your answer: ')
        if answ == corrct:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{corrct}'")
            print(f"Let's try again, {name}!")
            break

    if count == game.NUMBER_OF_ROUNDS:
        print(f'Congratulations, {name}!')
