import pytest
from functions.level_1.one_gender import genderalize


@pytest.fixture
def data_to_check_male_value() -> tuple[str, str, str, str]:
    return ("Пошел", "Пошла", "male", "Пошел")


@pytest.fixture
def data_to_check_female_value() -> tuple[str, str, str, str]:
    return ("Купил", "Купила", "female", "Купила")


def test__genderalize__check_if_male(
    data_to_check_male_value: tuple[str, str, str, str],
) -> None:
    verb_male = data_to_check_male_value[0]
    verb_female = data_to_check_male_value[1]
    gender = data_to_check_male_value[2]
    expected = data_to_check_male_value[3]
    assert genderalize(verb_male, verb_female, gender) == expected


def test__genderalize__check_if_female(
    data_to_check_female_value: tuple[str, str, str, str],
) -> None:
    verb_male = data_to_check_female_value[0]
    verb_female = data_to_check_female_value[1]
    gender = data_to_check_female_value[2]
    expected = data_to_check_female_value[3]
    assert genderalize(verb_male, verb_female, gender) == expected
