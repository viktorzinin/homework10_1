import os
import time

from src.generators import filter_by_currency
from src.processing import get_sorted, get_date_sorted, filter_dicts_by_string
from src.utils import get_transaction_json_data, get_transaction_csv_data, get_transaction_xlsx_data
from src.widget import get_new_data, mask_account_card


current_dir = os.path.dirname(os.path.abspath(__file__))


# print(mask_account_card("Visa Platinum 8990922113665229"))
#
# print(mask_account_card("Счет 35383033474447895560"))
#
# print(get_new_data("2018-07-11T02:26:18.671407"))
#
# print(
#     get_sorted(
#         [
#             {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
#
# print(
#     get_date_sorted(
#         (
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
# )
#
# # список словарей, для которых должны работать функции модуля generators:
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160",
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
# ]
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(3):
#     print(next(usd_transactions)["id"])
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))
#
# for card_number in card_number_generator(2, 7):
#     print(card_number)


# file_path = os.path.join(current_dir, "../data", "operations.json")
# transactions1 = transaction_amount(file_path)
#
#
# for transaction in transactions1:
#     rub_amount = currency_conversion(transaction)
#     print(f"Transaction amount in RUB: {rub_amount}")


def main():
    """Функция принимающая команды пользователя и возвращающая список транзакций, соответсвующих
    заданным пользователем параметрам"""
    list_of_commands = []
    print(
        """Привет!
    Добро пожаловать в программу работы с банковскими транзакциями."""
    )
    while len(list_of_commands) < 1:

        def status_command():
            """Функция принимает команду от пользователя и получает информацию о том, какой файл нужно открыть"""
            print(
                """Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла"""
            )
            answer = input()
            dict_of_file_types = {"1": "json", "2": "csv", "3": "xlsx"}
            if answer in dict_of_file_types.keys():
                print(f"Для обработки выбран {dict_of_file_types[answer].upper()}-файл.")
                list_of_commands.append(dict_of_file_types[answer])
            else:
                print("Некорректный ввод команды.")
            return list_of_commands

        list_of_commands = status_command()

    while len(list_of_commands) < 2:

        def operation_status():
            """Функция принимает от пользователя информацию о параметре статуса операции"""
            print(
                """
                        Введите статус, по которому необходимо выполнить фильтрацию.
                        Доступные для фильтровки статусы:
                        EXECUTED,
                        CANCELED,
                        PENDING"""
            )
            answer = input().lower()
            list_of_status = ["executed", "canceled", "pending"]
            if answer in list_of_status:
                print(f'Операции отфильтрованы по статусу "{answer.upper()}"')
                list_of_commands.append(answer.upper())
            else:
                print("Некорректный ввод команды.")
            return list_of_commands

        list_of_commands = operation_status()
    while len(list_of_commands) < 3:

        def sort_by_date_command():
            """Функция принимает от пользователя информацию о наличии параметра сортировки по дате"""
            print("Отсортировать операции по дате? Да/Нет")
            answer = input().lower()
            if answer in ["да", "нет"]:
                list_of_commands.append(answer)
            else:
                print("Некорректный ввод команды.")
            return list_of_commands

        list_of_commands = sort_by_date_command()
    while len(list_of_commands) < 4:

        def ascending():
            """Функция принимает от пользователя информацию о направлении сортировки по дате"""
            print("Отсортировать ПО ВОЗРАСТАНИЮ или ПО УБЫВАНИЮ даты?")
            answer = input().lower()
            if answer == "по возрастанию":
                list_of_commands.append(False)
            elif answer == "по убыванию":
                list_of_commands.append(True)
            else:
                print("Некорректный ввод команды.")
                return list_of_commands
            return list_of_commands

        if list_of_commands[2] == "да":
            list_of_commands = ascending()
        else:
            list_of_commands.append("")
    while len(list_of_commands) < 5:

        def currency_rub_command():
            """Функция принимает от пользователя параметр фитрации по валюте"""
            print("Выводить только рублевые тразакции? Да/Нет")
            answer = input().lower()
            if answer in ["да", "нет"]:
                list_of_commands.append(f"только рублёвые транзакции - {answer}")
            else:
                print("Некорректный ввод команды.")
                return list_of_commands
            return list_of_commands

        list_of_commands = currency_rub_command()
    while len(list_of_commands) < 6:

        def filter_by_word_command():
            """Функция принимает от пользователя информацию о параметре фильтрации по слову"""
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            answer = input().lower()
            if answer in ["да", "нет"]:
                list_of_commands.append(answer)
                if answer == "да":
                    print("Введите слово для фильтрации:")
                    answer = input().lower()
                    list_of_commands.append(answer)

            else:
                print("Некорректный ввод команды.")
            return list_of_commands

        list_of_commands = filter_by_word_command()

    def get_transactions_info():
        """Функция получает данные о транзакциях из выбранного файла"""
        if list_of_commands[0] == "json":
            path_to_json = os.path.join(current_dir, "../data", "operations.json")
            data = get_transaction_json_data(path_to_json)
        elif list_of_commands[0] == "csv":
            path_to_csv = os.path.join(current_dir, "../data", "transactions.csv")
            data = get_transaction_csv_data(path_to_csv)
        elif list_of_commands[0] == "xlsx":
            path_to_xlsx = os.path.join(current_dir, "../data", "transactions_excel.xlsx")
            data = get_transaction_xlsx_data(path_to_xlsx)
        else:
            data = []
        return data

    transactions_list = get_transactions_info()
    # информация о параметре статуса операции
    transactions_list = get_sorted(transactions_list, state=list_of_commands[1])
    # информацию о наличии параметра сортировки по дате
    if list_of_commands[2] == "да":
        transactions_list = get_date_sorted(transactions_list, reverse=list_of_commands[3])
    if list_of_commands[4] == "да":
        transactions_list = filter_by_currency(transactions_list, "руб.")
    if list_of_commands[5] == "да":
        transactions_list = filter_dicts_by_string(transactions_list, list_of_commands[6])

    masked_transactions_list = []
    masked_transaction_list = []

    if list_of_commands[0] == "json":
        not_empty_transactions = []
        for transaction in transactions_list:
            if "date" in transaction and "state" in transaction:
                not_empty_transactions.append(transaction)
        transactions_list = not_empty_transactions
        for transaction in transactions_list:
            modified_date = get_new_data(transaction["date"])
            masked_transaction_list.append(f"{modified_date}  {transaction['description']}")
            masked_account_to = mask_account_card(transaction["to"])
            if "from" in transaction:
                masked_account_from = mask_account_card(transaction["from"])
                masked_transaction_list.append(f"{masked_account_from} -> {masked_account_to}")
            else:
                masked_transaction_list.append(masked_account_to)
            masked_transaction_list.append(
                f"Сумма {transaction['operationAmount']['amount']} "
                f"{transaction['operationAmount']['currency']['name']}"
            )
            masked_transactions_list.append(masked_transaction_list)
    elif list_of_commands[0] == "csv":
        for transaction in transactions_list:
            if len(transaction["date"]) > 0:
                modified_date = get_new_data(transaction["date"])
                masked_transaction_list.append(f"{modified_date}  {transaction['description']}")
                masked_account_to = mask_account_card(transaction["to"])
                if transaction["from"]:
                    masked_account_from = mask_account_card(transaction["from"])
                    masked_transaction_list.append(f"{masked_account_from} -> {masked_account_to}")
                else:
                    masked_transaction_list.append(masked_account_to)
                masked_transaction_list.append(f"Сумма {transaction['amount']} " f"{transaction['currency_code']}")
                masked_transactions_list.append(masked_transaction_list)
    else:
        for transaction in transactions_list:
            if len(str(transaction["id"])) > 0:
                modified_date = get_new_data(transaction["date"])
                masked_transaction_list.append(f"{modified_date} {transaction['description']}")
                masked_account_to = mask_account_card(transaction["to"])
                if transaction["description"] != "Открытие вклада":
                    masked_account_from = mask_account_card(transaction["from"])
                    masked_transaction_list.append(f"{masked_account_from} -> {masked_account_to}")
                else:
                    masked_transaction_list.append(masked_account_to)
                masked_transaction_list.append(f"Сумма {int(transaction['amount'])} {transaction['currency_name']}")
                masked_transactions_list.append(masked_transaction_list)

    print(f"Открытие {list_of_commands[0]}-файла............")
    time.sleep(2)
    print("Фильтрация по указанным параметрам............")
    time.sleep(2)
    print("Сортировка по указанным параметрам............")
    time.sleep(2)
    print("Распечатываю список транзакций............")
    time.sleep(2)

    if len(masked_transactions_list) > 0:
        for transaction in masked_transactions_list:
            print("\n".join(transaction))
    else:
        print("\n\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
