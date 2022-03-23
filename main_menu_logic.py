from setting.all_setting import MAIN_MENU_TEXT, SELECT_OPTION, OPTION_RANGE, OUT_OF_RANGE
from setting.output_messages import return_menu_text, return_messages_for_player


def displaying_main_menu():
    for counter in range(len(MAIN_MENU_TEXT)):
        print(return_menu_text(MAIN_MENU_TEXT[counter]))


def selecting_option():
    while True:

        player_answer = input(return_messages_for_player(SELECT_OPTION))
        checking_player_answer = checking_correctness_selected_range(player_answer)

        if checking_player_answer[0] == None and checking_player_answer[1] != None:
            return checking_player_answer[1]

        elif checking_player_answer[0] != None and checking_player_answer[1] == None:
            return checking_player_answer[0]


def checking_correctness_selected_range(player_answer):
    """:return tupla(string,int)"""
    if player_answer >= OPTION_RANGE[0] and player_answer <= OPTION_RANGE[1]:
        return (None, player_answer)
    else:
        return (OUT_OF_RANGE, None)
