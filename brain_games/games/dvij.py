import prompt

from brain_games.games.calc_2 import question, gm_answ
from brain_games.games.nod import rand_digit, gm_ans


def general_logic(key):
    if key == 'key_calc':  # Условие для игры - Калькулятор
        game_answ = gm_answ
        correct = question
        first_question = 'What is the result of the expression?'

    elif key == 'key_nod':  # Условие для игры - НОД
        game_answ = gm_ans
        correct = rand_digit
        first_question = 'What is the result of the expression?'

        print('Welcome to the Brain Games!')
        name = prompt.string('May I have your name? ')
        print(f'Hello, {name}!')
        print(first_question)

        count = 0
        for i in range(3):
            c = correct()
            a = game_answ()
            if a == c:
                print('Correct!')
                count += 1
            elif a != c:
                print(c)
                print(f"'{a}' is wrong answer ;(. Correct answer was '{c}'")
                print(f"Let's try again, {name}!")
                break
            else:
                print(f"'{a}' is wrong answer ;(. Correct answer was '{c}'")
                print(f"Let's try again, {name}!")
                break

        if count == 3:
            print(f'Congratulations, {name}!')
