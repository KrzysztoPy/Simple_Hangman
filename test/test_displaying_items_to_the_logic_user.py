import pytest
from displaying_items_to_the_logic_user import displaying_one_element


@pytest.mark.parametrize("samples,expected", (
        ("",),
        ("Sample text"),

))
def test_displaying_one_element():
    displaying_one_element()
