import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import transaction_amount


class TestGetTransactions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_transaction_amount_valid_file(self, mock_file: MagicMock) -> None:
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_transaction_amount_invalid_content(self, mock_file: MagicMock) -> None:
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='{"transaction": "data"}')
    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_transaction_amount_json_decode_error(self, mock_json_load: MagicMock, mock_file: MagicMock) -> None:
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_transaction_amount_file_not_found(self, mock_file: MagicMock) -> None:
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
