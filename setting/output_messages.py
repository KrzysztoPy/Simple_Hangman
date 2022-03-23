from setting.all_setting import TEXT_COLOR_FOR_USER, TEXT_COLOR_FOR_PROGRAMMER, TEXT_COLOR_MAIN_MENU, \
    WARNING_COLOR_FOR_USER


def return_messages_for_player(message):
    print(TEXT_COLOR_FOR_USER + message)


def return_warning_for_player(message):
    print(WARNING_COLOR_FOR_USER + message)


def return_messages_for_programmer(message):
    print(TEXT_COLOR_FOR_PROGRAMMER + message)


def return_menu_text(menu_color_text):
    print(TEXT_COLOR_MAIN_MENU + menu_color_text)
