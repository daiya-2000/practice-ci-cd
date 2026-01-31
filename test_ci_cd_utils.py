import pytest

from ci_cd_utils import calculate_total


@pytest.mark.parametrize(
    "price, tax_rate, expected",
    [
        (1000, 0.1, 1100.0),
        (500, 0.08, 540.0),
        (0, 0.1, 0.0),
    ],
)
def test_calculate_total_success(price, tax_rate, expected):
    assert calculate_total(price, tax_rate) == expected


def test_calculate_total_default_tax_rate():
    assert calculate_total(1000) == 1100.0


@pytest.mark.parametrize(
    "price, tax_rate",
    [
        (-1, 0.1),
        (100, -0.1),
    ],
)
def test_calculate_total_negative_value(price, tax_rate):
    with pytest.raises(ValueError):
        calculate_total(price, tax_rate)


@pytest.mark.parametrize(
    "price, tax_rate",
    [
        ("100", 0.1),
        (100, "0.1"),
    ],
)
def test_calculate_total_non_number(price, tax_rate):
    with pytest.raises(ValueError):
        calculate_total(price, tax_rate)
