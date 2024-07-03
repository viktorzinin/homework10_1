import os.path

from src.widget import get_new_data, mask_account_card
from src.processing import get_sorted, get_date_sorted
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.utils import transaction_amount
from src.external_api import currency_conversion
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_csv = os.path.join(current_dir, "data", "transactions.csv")
path_to_xlsx = os.path.join(current_dir, "data", "transactions_excel.xlsx")

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

# список словарей, для которых должны работать функции модуля generators:
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions)["id"])

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(2, 7):
    print(card_number)


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "operations.json")
transactions1 = transaction_amount(file_path)


for transaction in transactions1:
    rub_amount = currency_conversion(transaction)
    print(f'Transaction amount in RUB: {rub_amount}')


def get_transaction_csv_data(path_to_csv):
    """Функция принимает путь до файла CSV и возвращает данные транзакций"""
    with open(path_to_csv, "r", encoding="utf-8") as file:
        data = pd.read_csv(file)
        data_as_dict = data.to_dict(orient="records")
        return data_as_dict


def get_transaction_xlsx_data(path_to_xlsx):
    """Функция принимает путь до файла XLSX и возвращает данные транзакций"""
    with open(path_to_xlsx, "rb") as file:
        data = pd.read_excel(file)
        data_as_dict = data.to_dict(orient="records")
        return data_as_dict


if __name__ == "__main__":
    data = get_transaction_csv_data(path_to_csv)
    print(data)
    data = get_transaction_xlsx_data(path_to_xlsx)
    print(data)
