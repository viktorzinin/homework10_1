import pytest
from src.widget import get_new_data


@pytest.fixture
def old_data():
    return "2018-07-11T02:26:18.671407"


def test_get_new_data(old_data):
    assert get_new_data(old_data) == "11.07.2018"
