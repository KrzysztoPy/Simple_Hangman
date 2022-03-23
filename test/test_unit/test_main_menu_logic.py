from setting.all_setting import SELECT_OPTION
from main_menu_logic import selecting_option, checking_correctness_selected_range
import pytest

pytest.mark.parametrize("sample",
                        (0, 1, 4, 5))


def test_select_option():
    pass


@pytest.mark.parametrize("range,expected", (
        (0, (f"Selected option is out of range. {SELECT_OPTION}")),
        (1, 1),
        (4, 4),
        (5, (f"Selected option is out of range. {SELECT_OPTION}"))
))
def test_selecting_option(range, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: range)
    result = selecting_option()
    assert result == expected


@pytest.mark.parametrize("range,expected", (
        (0, (f"Selected option is out of range. {SELECT_OPTION}", None)),
        (1, (None, 1)),
        (4, (None, 4)),
        (5, (f"Selected option is out of range. {SELECT_OPTION}", None))
))
def test_checking_correctness_selected_range(range, expected):
    result = checking_correctness_selected_range(range)
    assert result == expected
    assert len(result) == 2
