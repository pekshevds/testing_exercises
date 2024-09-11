import pytest
from datetime import datetime, date, timedelta
from functions.level_1.two_date_parser import compose_datetime_from

# Сегодня строкой
today_str: str = datetime.strftime(date.today(), "%d-%m-%Y")
# Завтра строкой
tomorrow_str: str = datetime.strftime(date.today() + timedelta(days=1), "%d-%m-%Y")
# Текущий формат даты
carrent_date_format: str = "%d-%m-%Y %H:%M"


@pytest.mark.parametrize(
    "date_str,time_str,expected",
    [
        (
            today_str,  # date_str
            "08:35",  # time_str
            datetime.strptime(f"{today_str} 08:35", carrent_date_format),  # expected
        ),
        (
            today_str,  # date_str
            "23:59",  # time_str
            datetime.strptime(
                f"{today_str} 23:59",
                carrent_date_format,
            ),  # expected
        ),
        (
            today_str,  # date_str
            "00:01",  # time_str
            datetime.strptime(
                f"{today_str} 00:01",
                carrent_date_format,
            ),  # expected
        ),
        (
            "tomorrow",  # date_str
            "00:01",  # time_str
            datetime.strptime(
                f"{tomorrow_str} 00:01",
                carrent_date_format,
            ),  # expected
        ),
    ],
)
def test_compose_datetime_from(
    date_str: str, time_str: str, expected: datetime
) -> None:
    assert compose_datetime_from(date_str, time_str) == expected


def test_compose_datetime_from_if_today() -> None:
    expected: datetime = datetime.strptime(f"{today_str} 08:35", carrent_date_format)
    assert compose_datetime_from(today_str, "08:35") == expected


def test_compose_datetime_from_if_tomorrow() -> None:
    expected: datetime = datetime.strptime(f"{tomorrow_str} 00:01", carrent_date_format)
    assert compose_datetime_from("tomorrow", "00:01") == expected
