# Information from https://stackabuse.com/how-to-print-colored-text-in-python/
# output_messages: Print color messsage
TEXT_COLOR_FOR_USER = "\033[34m"  # Blue
WARNING_COLOR_FOR_USER = "\033[33m"  # Yellow
TEXT_COLOR_FOR_PROGRAMMER = "\033[31m"  # Red
TEXT_COLOR_MAIN_MENU = "\033[1;32m"  # GREEN

"""__________________________________________________________________________________________________________________"""
# main_menu_logic
""" SCHEMA: 
        OPTIONS_RANGE: Gets the first number of each element from MAIN_MENU_TEXT 
"""
MAIN_MENU_TEXT = "1. Start game".upper(), "2. Score board".upper(), "3. Load game".upper(), "4. Exit game".upper()
OPTION_RANGE = int(MAIN_MENU_TEXT[0][0]), int(MAIN_MENU_TEXT[3][0])
SELECT_OPTION = f"Select option {OPTION_RANGE[0]} - {OPTION_RANGE[1]}:"
OUT_OF_RANGE = f"Selected option is out of range. {SELECT_OPTION}"
EXPECTED_INSTANCE = int
WRONG_TYPE = f"Not selected int option from the scope was not selected {OPTION_RANGE[0]} - {OPTION_RANGE[1]}." \
             f" Please, try again!"

"""__________________________________________________________________________________________________________________"""
#
MINIMUM_SCREEN_RESOLUTION = 1024, 600
"""__________________________________________________________________________________________________________________"""
