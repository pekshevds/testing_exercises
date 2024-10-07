import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.fixture
def github_pull_url() -> str:
    return "https://github.com/pekshevds/tic-tac-toe/pull/1"


@pytest.fixture
def github_not_pull_url() -> str:
    return "https://github.com/pekshevds/tic-tac-toe"


@pytest.fixture
def not_github_url() -> str:
    return "https://yandex.ru"


def test__is_github_pull_request_url__check_correct_url(
    github_pull_url: str,
) -> None:
    assert is_github_pull_request_url(github_pull_url) is True


def test__is_github_pull_request_url__check_not_pull_url(
    github_not_pull_url: str,
) -> None:
    assert is_github_pull_request_url(github_not_pull_url) is False


def test__is_github_pull_request_url__check_not_github_url(
    not_github_url: str,
) -> None:
    assert is_github_pull_request_url(not_github_url) is False
