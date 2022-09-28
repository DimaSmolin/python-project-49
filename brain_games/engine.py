import prompt


#  Это движок,

def starts_games(correct, game_instructions):
    number_of_rounds = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_instructions)

    count = 0
    for i in range(number_of_rounds):
        corrct = correct.question()
        answ = prompt.string('Your answer: ')
        if answ == corrct:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{corrct}'")
            print(f"Let's try again, {name}!")
            break

    if count == number_of_rounds:
        print(f'Congratulations, {name}!')
