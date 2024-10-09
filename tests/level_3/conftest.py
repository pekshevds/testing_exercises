import pytest
import decimal
import datetime
from functions.level_3.models import Expense, BankCard, ExpenseCategory, Currency


@pytest.fixture
def bank_cards() -> list[BankCard]:
    return [
        BankCard(last_digits="748745", owner="Sasha"),
        BankCard(last_digits="999548", owner="Misha"),
        BankCard(last_digits="001244", owner="Igor"),
    ]


@pytest.fixture
def expense1(bank_cards: list[BankCard]) -> Expense:
    return Expense(
        amount=decimal.Decimal(10.5),
        currency=Currency.RUB,
        card=bank_cards[0],
        spent_in="cafe",
        spent_at=datetime.datetime.strptime("1.08.24", "%d.%m.%y"),
        category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
    )


@pytest.fixture
def expense2(bank_cards: list[BankCard]) -> Expense:
    return Expense(
        amount=decimal.Decimal(168.5),
        currency=Currency.RUB,
        card=bank_cards[1],
        spent_in="pharmacy",
        spent_at=datetime.datetime.strptime("21.09.24", "%d.%m.%y"),
        category=ExpenseCategory.MEDICINE_PHARMACY,
    )


@pytest.fixture
def expense3(bank_cards: list[BankCard]) -> Expense:
    return Expense(
        amount=decimal.Decimal(300.0),
        currency=Currency.RUB,
        card=bank_cards[2],
        spent_in="food and vine",
        spent_at=datetime.datetime.strptime("21.09.24", "%d.%m.%y"),
        category=ExpenseCategory.BAR_RESTAURANT,
    )


@pytest.fixture
def expenses(expense1: Expense, expense2: Expense, expense3: Expense) -> list[Expense]:
    return [
        expense1,
        expense2,
        expense3,
    ]
