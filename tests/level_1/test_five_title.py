import pytest
from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title,max_main_item_title_length,expected",
    [
        ("Copy of (1) (2) (3) (4)", 7, "Copy of (1) (2) (3) (4)"),  # len condition
        ("(1) (2) (3) (4)", 100, "Copy of (1) (2) (3) (4)"),  # startwith condition
        ("Copy of 1 2 3 4", 100, "Copy of 1 2 3 4 (2)"),  # return False
        ("Copy of (1) (2) (3) (4)", 100, "Copy of (1) (2) (3) (5)"),  # return True
    ],
)
def test_change_copy_item(title: str, max_main_item_title_length: int, expected: str):
    assert change_copy_item(title, max_main_item_title_length) == expected
