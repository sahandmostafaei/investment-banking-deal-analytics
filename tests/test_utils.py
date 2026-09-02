from src.utils import (
    format_currency,
    format_percentage,
)


def test_format_currency():

    result = format_currency(1234567.89)

    assert result == "$1,234,567.89"


def test_format_percentage():

    result = format_percentage(0.125)

    assert result == "12.50%"
