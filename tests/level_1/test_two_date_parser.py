import pytest
import datetime
from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    "date_str,time_str,expected",
    [
        (
            datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y"),  # date_str
            "08:35",  # time_str
            datetime.datetime.strptime(
                f"{datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y")} 08:35",
                "%d-%m-%Y %H:%M",
            ),  # expected
        ),
        (
            datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y"),  # date_str
            "23:59",  # time_str
            datetime.datetime.strptime(
                f"{datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y")} 23:59",
                "%d-%m-%Y %H:%M",
            ),  # expected
        ),
        (
            datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y"),  # date_str
            "00:01",  # time_str
            datetime.datetime.strptime(
                f"{datetime.datetime.strftime(datetime.date.today(), "%d-%m-%Y")} 00:01",
                "%d-%m-%Y %H:%M",
            ),  # expected
        ),
        (
            "tomorrow",  # date_str
            "00:01",  # time_str
            datetime.datetime.strptime(
                f"{datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days=1), "%d-%m-%Y")} 00:01",
                "%d-%m-%Y %H:%M",
            ),  # expected
        ),
    ],
)
def test_compose_datetime_from(
    date_str: str, time_str: str, expected: datetime.datetime
):
    assert compose_datetime_from(date_str, time_str) == expected
