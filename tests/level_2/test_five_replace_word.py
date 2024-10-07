import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.fixture
def text() -> str:
    return (
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
        "It has survived not only five centuries, but also the leap into electronic typesetting, "
        "remaining essentially unchanged. It was popularised in the 1960s with the release of "
        "Letraset sheets containing Lorem Ipsum passages, and more recently with desktop "
        "publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    )


@pytest.fixture
def replace_from() -> str:
    return "Lorem"


@pytest.fixture
def fake_replace_from() -> str:
    return "John"


@pytest.fixture
def replace_to() -> str:
    return "John"


def test__replace_word__check_that_the_text_doest_contain_replacement_word(
    text: str, replace_from: str, replace_to: str
) -> None:
    assert replace_word(text, replace_from, replace_to) != text


def test__replace_word__check_that_the_text_doest_contain_desired_word(
    text: str, fake_replace_from: str, replace_to: str
) -> None:
    assert replace_word(text, fake_replace_from, replace_to) == text
