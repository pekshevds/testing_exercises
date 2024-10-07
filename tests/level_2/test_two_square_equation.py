import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.fixture
def data_discriminant_less_zero() -> dict[str, float]:
    return {
        "square_coefficient": 4.0,
        "linear_coefficient": 2.0,
        "const_coefficient": 1.0,
    }


@pytest.fixture
def data_square_coefficient_equal_zero() -> dict[str, float]:
    return {
        "square_coefficient": 0.0,
        "linear_coefficient": 2.0,
        "const_coefficient": 1.0,
    }


@pytest.fixture
def data_both_square_coefficient_and_linear_coefficient_equal_zero() -> (
    dict[str, float]
):
    return {
        "square_coefficient": 0.0,
        "linear_coefficient": 0.0,
        "const_coefficient": 1.0,
    }


@pytest.fixture
def data_for_common_case() -> dict[str, float]:
    return {
        "square_coefficient": 2.0,
        "linear_coefficient": 6.0,
        "const_coefficient": 1.0,
    }


def test__solve_square_equation__discriminant_less_zero(
    data_discriminant_less_zero: dict[str, float],
) -> None:
    root_left, root_right = solve_square_equation(**data_discriminant_less_zero)
    assert root_left is None and root_right is None


def test__solve_square_equation__square_coefficient_equal_zero(
    data_square_coefficient_equal_zero: dict[str, float],
) -> None:
    root_left, root_right = solve_square_equation(**data_square_coefficient_equal_zero)
    assert root_left is not None and root_right is None


def test__solve_square_equation__square_coefficient_and_linear_coefficient_equal_zero(
    data_both_square_coefficient_and_linear_coefficient_equal_zero: dict[str, float],
) -> None:
    root_left, root_right = solve_square_equation(
        **data_both_square_coefficient_and_linear_coefficient_equal_zero
    )
    assert root_left is None and root_right is None


def test__solve_square_equation__calculate_common_case(
    data_for_common_case: dict[str, float],
) -> None:
    root_left, root_right = solve_square_equation(**data_for_common_case)
    assert root_left is not None and root_right is not None
