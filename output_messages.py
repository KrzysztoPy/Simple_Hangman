from all_setting import TEXT_COLOR_FOR_USER, TEXT_COLOR_FOR_PROGRAMMER, TEXT_COLOR_MAIN_MENU


def messages_for_player(message):
    return TEXT_COLOR_FOR_USER + message


def messages_for_programmer(message):
    return TEXT_COLOR_FOR_PROGRAMMER + message


def menu_text(menu_color_text):
    return TEXT_COLOR_MAIN_MENU + menu_color_text
