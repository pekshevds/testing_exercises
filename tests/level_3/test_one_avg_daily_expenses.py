import pytest
import decimal
import datetime
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_3.models import Expense, BankCard, ExpenseCategory, Currency


@pytest.fixture
def bank_cards() -> list[BankCard]:
    return [
        BankCard(last_digits="748745", owner="Sasha"),
        BankCard(last_digits="999548", owner="Misha"),
        BankCard(last_digits="001244", owner="Igor"),
    ]


@pytest.fixture
def expenses(bank_cards: list[BankCard]) -> list[Expense]:
    return [
        Expense(
            amount=decimal.Decimal("10.5"),
            currency=Currency.RUB,
            card=bank_cards[0],
            spent_in="cafe",
            spent_at=datetime.datetime.strptime("1.08.24", "%d.%m.%y"),
            category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
        ),
        Expense(
            amount=decimal.Decimal("168.5"),
            currency=Currency.RUB,
            card=bank_cards[1],
            spent_in="pharmacy",
            spent_at=datetime.datetime.strptime("21.09.24", "%d.%m.%y"),
            category=ExpenseCategory.MEDICINE_PHARMACY,
        ),
        Expense(
            amount=decimal.Decimal("300.0"),
            currency=Currency.RUB,
            card=bank_cards[2],
            spent_in="food and vine",
            spent_at=datetime.datetime.strptime("21.09.24", "%d.%m.%y"),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
    ]


def test__calculate_average_daily_expenses__(expenses: list[Expense]) -> None:
    assert calculate_average_daily_expenses(expenses) == decimal.Decimal("239.5")
