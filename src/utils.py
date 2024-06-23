import json
import logging


logging.basicConfig(
    filename="logs/application.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger('utils')


def transaction_amount(file_path: str) -> list:
    """Функцию, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            logger.info("Возвращает список словарей")
            return repos
        else:
            logger.info("Фаил пустой, содержит не список или не найден")
            return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        print(f"Ошибка {e}")
        return []
