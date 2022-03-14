from all_setting import MAIN_MENU_TEXT
from output_messages import return_menu_text


def displaying_main_menu():
    for counter in range(len(MAIN_MENU_TEXT)):
        print(return_menu_text(MAIN_MENU_TEXT[counter]))
