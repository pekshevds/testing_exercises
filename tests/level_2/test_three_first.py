from typing import Any
import pytest
from functions.level_2.three_first import first, NOT_SET


@pytest.fixture
def items_isnt_empty() -> dict[str, Any]:
    return {"items": [1, 2, 3], "default": 1}


@pytest.fixture
def items_is_empty() -> dict[str, Any]:
    return {"items": None, "default": 1}


@pytest.fixture
def for_exception() -> dict[str, Any]:
    return {"items": None, "default": NOT_SET}


def test__first__return_first_item_from_non_empty_list(
    items_isnt_empty: dict[str, Any],
) -> None:
    assert first(**items_isnt_empty) is not None


def test__first__return_default_value_if_items_is_empty(
    items_is_empty: dict[str, Any],
) -> None:
    assert first(**items_is_empty) == 1


def test__first__return_exception(
    for_exception: dict[str, Any],
) -> None:
    with pytest.raises(AttributeError):
        first(**for_exception)
