import prompt


#  Это движок,

def general_logics(answer, correct, first_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(first_question)

    count = 0
    for i in range(3):
        c = correct()
        a = answer()
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
