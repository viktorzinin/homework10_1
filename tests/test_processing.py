import pytest
from src.processing import get_sorted, get_date_sorted


def test_get_sort_dict(list_dict):
    assert get_sorted(list_dict) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
