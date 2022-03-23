import pytest
from setting import output_messages as om
from setting.all_setting import TEXT_COLOR_FOR_USER, TEXT_COLOR_FOR_PROGRAMMER, TEXT_COLOR_MAIN_MENU

for_test_color_text_for_user = "\033[34m"
for_test_color_text_for_programmer = "\033[31m"
for_test_color_text_for_main_menu = "\033[1;32m"


@pytest.mark.parametrize("message,expected", (
        ("Hello world", for_test_color_text_for_user + "Hello world"),
        ("Hello player one", for_test_color_text_for_user + "Hello player one")
))
def test_return_messages_for_player(message, expected):
    result = om.return_messages_for_player(message)
    assert for_test_color_text_for_user == TEXT_COLOR_FOR_USER
    assert result == expected


@pytest.mark.parametrize("message,expected", (
        ("Warning", for_test_color_text_for_programmer + "Warning"),
        ("First problem", for_test_color_text_for_programmer + "First problem")
))
def test_return_messages_for_programmer(message, expected):
    result = om.return_messages_for_programmer(message)
    assert for_test_color_text_for_programmer == TEXT_COLOR_FOR_PROGRAMMER
    assert result == expected


@pytest.mark.parametrize("message,expected", (
        ("1.Start game ", for_test_color_text_for_main_menu + "1.Start game "),
        ("3.Exit", for_test_color_text_for_main_menu + "3.Exit")
))
def test_return_menu_text(message, expected):
    result = om.return_menu_text(message)
    assert for_test_color_text_for_main_menu == TEXT_COLOR_MAIN_MENU
    assert result == expected
