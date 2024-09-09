import datetime
from decimal import Decimal
import pytest
from functions.level_1.four_bank_parser import (
    BankCard,
    SmsMessage,
    Expense,
    parse_ineco_expense,
)

date_format = "%d.%m.%y %H:%M"

bank_card1 = BankCard(last_digits="4321", owner="denis pekshev")
bank_card2 = BankCard(last_digits="4789", owner="john smith")
bank_card3 = BankCard(last_digits="7654", owner="sarah connor")


@pytest.mark.parametrize(
    "sms,cards,expected",
    [
        (
            SmsMessage(
                text="10000 99, 9874-2590-3658-4321 31.10.24 18:00 spent_in authcode 9874",
                author="denis pekshev",
                sent_at=datetime.datetime.strptime("31.10.24 18:00", date_format),
            ),
            [bank_card1, bank_card2, bank_card3],
            Expense(
                amount=Decimal("10000"),
                card=bank_card1,
                spent_in="spent_in",
                spent_at=datetime.datetime.strptime("31.10.24 18:00", date_format),
            ),
        ),
        (
            SmsMessage(
                text="5 00, 9874-2590-3658-7654 31.10.24 18:00 spent_in authcode 9874",
                author="sarah connor",
                sent_at=datetime.datetime.strptime("31.10.24 18:00", date_format),
            ),
            [bank_card1, bank_card2, bank_card3],
            Expense(
                amount=Decimal("5"),
                card=bank_card3,
                spent_in="spent_in",
                spent_at=datetime.datetime.strptime("31.10.24 18:00", date_format),
            ),
        ),
    ],
)
def test_parse_ineco_expense(sms: SmsMessage, cards: list[BankCard], expected: Expense):
    assert parse_ineco_expense(sms, cards) == expected
