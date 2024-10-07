import pytest
from datetime import datetime, date, timedelta
from functions.level_1.two_date_parser import compose_datetime_from

# Сегодня строкой
today_str: str = datetime.strftime(date.today(), "%d-%m-%Y")
# Завтра строкой
tomorrow_str: str = datetime.strftime(date.today() + timedelta(days=1), "%d-%m-%Y")
# Текущий формат даты
carrent_date_format: str = "%d-%m-%Y %H:%M"


@pytest.fixture
def data_to_check_if_today() -> dict[str, str | datetime]:
    return {
        "date_str": today_str,
        "time_str": "01:01",
        "expected": datetime.strptime(f"{today_str} 01:01", carrent_date_format),
    }


@pytest.fixture
def data_to_check_if_tomorrow() -> dict[str, str | datetime]:
    return {
        "date_str": "tomorrow",
        "time_str": "01:01",
        "expected": datetime.strptime(f"{tomorrow_str} 01:01", carrent_date_format),
    }


def test__compose_datetime_from__if_today(
    data_to_check_if_today: dict[str, str | datetime],
) -> None:
    date_str = str(data_to_check_if_today.get("date_str"))
    time_str = str(data_to_check_if_today.get("time_str"))
    expected = data_to_check_if_today.get("expected")
    assert compose_datetime_from(date_str, time_str) == expected


def test__compose_datetime_from__if_tomorrow(
    data_to_check_if_tomorrow: dict[str, str | datetime],
) -> None:
    date_str = str(data_to_check_if_tomorrow.get("date_str"))
    time_str = str(data_to_check_if_tomorrow.get("time_str"))
    expected = data_to_check_if_tomorrow.get("expected")
    assert compose_datetime_from(date_str, time_str) == expected
