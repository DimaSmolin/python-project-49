import prompt

NUMBER_OF_ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_MANUAL)

    count = 0
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.question_and_answer()
        print('Question:', str(question))
        gamer_answer = prompt.string('Your answer: ')
        if gamer_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{gamer_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        print(f'Congratulations, {name}!')
