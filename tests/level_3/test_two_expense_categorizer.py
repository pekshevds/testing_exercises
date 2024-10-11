import pytest
from functions.level_3.two_expense_categorizer import (
    guess_expense_category,
    is_string_contains_trigger,
)
from functions.level_3.models import Expense, ExpenseCategory


def test__guess_expense_category__check_value_equal_expected(expense2: Expense) -> None:
    assert guess_expense_category(expense2) == ExpenseCategory.MEDICINE_PHARMACY


def test__guess_expense_category__check_cafe_isnt_in_culture(expense1: Expense) -> None:
    assert guess_expense_category(expense1) != ExpenseCategory.THEATRES_MOVIES_CULTURE


@pytest.fixture
def original_string() -> str:
    return "every hunter wants to know where the pheasant is sitting"


def test__is_string_contains_trigger__check_string_contains_trigger(
    original_string: str,
) -> None:
    assert is_string_contains_trigger(original_string, "pheasant") is True


def test__is_string_contains_trigger__check_string_dont_contains_trigger(
    original_string: str,
) -> None:
    assert is_string_contains_trigger(original_string, "sparrow") is False
