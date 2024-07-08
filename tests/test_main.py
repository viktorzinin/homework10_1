from src.main import get_transaction_csv_data, get_transaction_xlsx_data
import unittest
from unittest.mock import MagicMock, mock_open, patch
import pandas as pd


class TestGetTransactionsCSV(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover 7269000803370165;"
        "American Express 1963030970727681;Перевод с карты на карту\n",
    )
    def test_get_transactions_info_csv(self, mock_file: MagicMock) -> None:
        result = get_transaction_csv_data("test.csv")
        self.assertEqual(
            result,
            [
                {
                    "id;state;date;amount;currency_name;currency_code;from;to;description":
                        "4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover "
                    "7269000803370165;American "
                    "Express "
                    "1963030970727681;Перевод "
                    "с "
                    "карты "
                    "на "
                    "карту"
                }
            ],
        )


class GetTransactionsInfoExcel(unittest.TestCase):
    data = {
        "id": [4699552.0],
        "state": ["EXECUTED"],
        "date": ["2022-03-23T08:29:37Z"],
        "amount": [23423.0],
        "currency_name": ["Peso"],
        "currency_code": ["PHP"],
        "from": ["Discover 7269000803370165"],
        "to": ["American Express 1963030970727681"],
        "description": ["Перевод с карты на карту"],
    }

    df = pd.DataFrame(data)

    df.to_excel("test.xlsx", index=False)

    @patch("pandas.read_excel", return_value=df)
    def test_get_transactions_info_xlsx(self, mock_read_excel: MagicMock) -> None:
        result = get_transaction_xlsx_data("test.xlsx")
        self.assertEqual(
            result,
            [
                {
                    "id": 4699552.0,
                    "state": "EXECUTED",
                    "date": "2022-03-23T08:29:37Z",
                    "amount": 23423.0,
                    "currency_name": "Peso",
                    "currency_code": "PHP",
                    "description": "Перевод с карты на карту",
                    "from": "Discover 7269000803370165",
                    "to": "American Express 1963030970727681",
                }
            ],
        )
