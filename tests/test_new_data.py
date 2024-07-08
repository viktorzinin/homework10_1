import pytest
from src.widget import get_new_data


@pytest.fixture
def old_data():
    return "2018-07-11T02:26:18.671407"


def test_get_new_data(old_data):
    assert get_new_data(old_data) == "11.07.2018"


@pytest.mark.parametrize(
    "old_data, result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.4255722", "30.06.2018"),
    ],
)
def test_get_new_data_1(old_data, result):
    assert get_new_data(old_data) == result
