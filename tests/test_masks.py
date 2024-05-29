import pytest
from src.widget import mask_account_card


@pytest.fixture
def number_card():
    return "1234567891234567"


@pytest.fixture
def number_account():
    return "Счет 35383033474447895566"


def test_mask_card(number_card):
    assert mask_account_card(number_card) == "1234 56** **** 4567"


def test_mask_account_card(number_account):
    assert mask_account_card(number_account) == "Счет **5566"


@pytest.fixture
def number_card_invalid():
    return "123456789123456"


def test_mask_account_card_invalid(number_card_invalid):
    with pytest.raises(ValueError):
        mask_account_card(number_card_invalid)
