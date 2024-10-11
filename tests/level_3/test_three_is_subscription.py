from functions.level_3.three_is_subscription import is_subscription
from functions.level_3.models import Expense


def test__is_subscription__check_is_subscription(
    expense4: Expense, expenses: list[Expense]
) -> None:
    assert is_subscription(expense4, expenses) is True


def test__is_subscription__check_isnt_subscription(
    expense1: Expense, expenses: list[Expense]
) -> None:
    assert is_subscription(expense1, expenses) is False
