from typing import Mapping
import pytest
from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,expected",
    [
        (
            "localhost",
            "part1/part2",
            {"id": "1", "name": "some-name", "value": "some-value"},
            "localhost/part1/part2?id=1&name=some-name&value=some-value",
        ),
        (
            "localhost",
            "part1/part2",
            None,
            "localhost/part1/part2",
        ),
    ],
)
def test_build_url(
    host_name: str,
    relative_url: str,
    get_params: Mapping[str, str],
    expected: str,
) -> None:
    assert build_url(host_name, relative_url, get_params) == expected


def test_build_url_with_full_params() -> None:
    host_name = "localhost"
    relative_url = "part1/part2"
    get_params = {"id": "1", "name": "some-name", "value": "some-value"}
    expected = "localhost/part1/part2?id=1&name=some-name&value=some-value"
    assert build_url(host_name, relative_url, get_params) == expected


def test_build_url_without_params() -> None:
    host_name = "localhost"
    relative_url = "part1/part2"
    get_params: dict = {}
    expected = "localhost/part1/part2"
    assert build_url(host_name, relative_url, get_params) == expected


def test_build_url_with_only_id_param() -> None:
    host_name = "localhost"
    relative_url = "part1/part2"
    get_params: dict = {"id": "1"}
    expected = "localhost/part1/part2?id=1"
    assert build_url(host_name, relative_url, get_params) == expected
