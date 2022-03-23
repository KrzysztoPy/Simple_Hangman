from setting.all_setting import OPTION_RANGE, OUT_OF_RANGE


def correctness_data_type_entered_data(data, expected_instance):
    try:
        expected_instance(data)
        return True
    except ValueError:
        return False


def checking_correctness_selected_range(player_answer):
    """:return tupla(string,int)"""
    if player_answer >= OPTION_RANGE[0] and player_answer <= OPTION_RANGE[1]:
        return (player_answer, None)
    else:
        return (None, OUT_OF_RANGE)
