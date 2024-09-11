import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,expected",
    [
        ("Пошел", "Пошла", "male", "Пошел"),
        ("Купил", "Купила", "female", "Купила"),
        ("Тестировал", "Тестировала", "female", "Тестировала"),
        ("Бегал", "Бегала", "male", "Бегал"),
    ],
)
def test_genderalize(verb_male: str, verb_female: str, gender: str, expected: str):
    assert genderalize(verb_male, verb_female, gender) == expected
