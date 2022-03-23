import pytest
from setting.checking_the_correctness_of_entered_data import checking_correctness_selected_range, \
    correctness_data_type_entered_data
from setting.all_setting import SELECT_OPTION


@pytest.mark.parametrize("data,type,expected", (
        (0, int, True),
        (1, int, True),
        ("z", str, True),
        ("z", int, False),
        ("$", int, False),
        (" ", int, False),

))
def test_correctness_data_type_entered_data(data, type, expected):
    result = correctness_data_type_entered_data(data, type)
    assert result == expected


@pytest.mark.parametrize("range,expected", (
        (0, (None, f"Selected option is out of range. {SELECT_OPTION}")),
        (1, (1, None)),
        (4, (4, None)),
        (5, (None, f"Selected option is out of range. {SELECT_OPTION}"))
))
def test_checking_correctness_selected_range(range, expected):
    result = checking_correctness_selected_range(range)
    assert result == expected
    assert len(result) == 2
