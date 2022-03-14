import pytest
from shared_element.common_parts_logic import get_answer_for_the_user, set_time_for_answer


@pytest.mark.parametrize()
def test_get_answer_for_the_user():
    pass


@pytest.mark.skip
@pytest.mark.parametrize("samples", (
        {},
        {"A": "10"},
        {"A": "10", "B": "20", "C": "30"},
))
def test_set_time_for_answer():
    pass
