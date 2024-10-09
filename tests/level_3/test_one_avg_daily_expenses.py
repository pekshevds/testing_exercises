import decimal
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_3.models import Expense


def test__calculate_average_daily_expenses__check_value_equal_expected(
    expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(expenses) == decimal.Decimal(239.5)
