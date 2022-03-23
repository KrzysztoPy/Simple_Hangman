from setting.all_setting import MAIN_MENU_TEXT, SELECT_OPTION, EXPECTED_INSTANCE, WRONG_TYPE
from setting.output_messages import return_menu_text, return_messages_for_player, return_warning_for_player
from setting.checking_the_correctness_of_entered_data import correctness_data_type_entered_data, \
    checking_correctness_selected_range


def displaying_main_menu():
    for counter in range(len(MAIN_MENU_TEXT)):
        return_menu_text(MAIN_MENU_TEXT[counter])


def selecting_option():
    while True:
        return_messages_for_player(SELECT_OPTION)
        player_answer = input()

        if correctness_data_type_entered_data(player_answer, EXPECTED_INSTANCE):
            checking_player_answer = checking_correctness_selected_range(EXPECTED_INSTANCE(player_answer))

            if checking_player_answer[0] != None and checking_player_answer[1] == None:
                return checking_player_answer[0]

            elif checking_player_answer[0] == None and checking_player_answer[1] != None:
                return_warning_for_player(checking_player_answer[1])
        else:
            return_warning_for_player(WRONG_TYPE)
