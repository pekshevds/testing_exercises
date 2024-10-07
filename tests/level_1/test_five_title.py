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
def test_change_copy_item(
    title: str, max_main_item_title_length: int, expected: str
) -> None:
    assert change_copy_item(title, max_main_item_title_length) == expected


def test_change_copy_item_if_len_of_title_is_more_or_equals_than_max_main_item_title_length() -> (
    None
):
    assert (
        change_copy_item(title="Copy of (1) (2) (3) (4)", max_main_item_title_length=7)
        == "Copy of (1) (2) (3) (4)"
    )


def test_change_copy_item_if_title_startswith() -> None:
    assert change_copy_item(title="(1) (2) (3) (4)") == "Copy of (1) (2) (3) (4)"


def test_change_copy_item_if_has_copy_number_negative() -> None:
    assert change_copy_item(title="Copy of 1 2 3 4") == "Copy of 1 2 3 4 (2)"


def test_change_copy_item_if_has_copy_number_positive() -> None:
    assert (
        change_copy_item(title="Copy of (1) (2) (3) (4)") == "Copy of (1) (2) (3) (5)"
    )
