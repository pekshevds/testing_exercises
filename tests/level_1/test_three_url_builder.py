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
):
    assert build_url(host_name, relative_url, get_params) == expected
