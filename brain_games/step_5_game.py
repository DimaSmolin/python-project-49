from random import randint

import prompt


def guess_the_honesty():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    for i in range(3):

        num = randint(1, 100)
        print('Question:', num)
        gamer_answr = prompt.string('Your answer: ')

        if num % 2 == 0 and gamer_answr == 'yes':
            count += 1
            print('correct')
        elif num % 2 == 1 and gamer_answr == 'no':
            count += 1
            print('correct')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
