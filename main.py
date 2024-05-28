from src.widget import get_new_data, mask_account_card
from src.processing import get_sorted, get_date_sorted

print(mask_account_card("Visa Platinum 8990922113665229"))

print(mask_account_card("Счет 35383033474447895560"))

print(get_new_data("2018-07-11T02:26:18.671407"))

print(
    get_sorted(
        [
            {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(
    get_date_sorted(
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
)
