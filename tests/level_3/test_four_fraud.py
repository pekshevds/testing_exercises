from functions.level_3.four_fraud import find_fraud_expenses
from functions.level_3.models import Expense


def test__find_fraud_expenses__check_that_expences_contains_fraud(
    expenses_with_fraud: list[Expense],
) -> None:
    assert find_fraud_expenses(expenses_with_fraud) != []


def test__find_fraud_expenses__expences_doest_contains_fraud_items(
    expenses: list[Expense],
) -> None:
    assert find_fraud_expenses(expenses) == []
