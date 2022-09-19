from brain_games.games.calc_2 import question, gm_answ, corr_ans


def general_logics(key):
    #    global quest, game_answ
    if key == 'key_calc':
        quest = question
        game_answ = gm_answ
        corrent = corr_ans

        print('Question:', quest())
        x = game_answ()
        y = corrent()
        print('corent', corrent())
        print('answer', x)

        print(type(y))
        print(type(x))
