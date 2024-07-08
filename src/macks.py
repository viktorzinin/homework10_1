from src.logger import setup_logger
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_logs = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_logs)


def get_mask_card(number: str) -> str:
    """
    Функция принимает строку
    :param number:str
    :return: маску карты
    """
    logger.info("Принимаем номер карты:")
    number_cards = f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    logger.info(f"Возвращаем маску карты: {number_cards}")
    return number_cards


def get_mask_account(number: str) -> str:
    """
    Функция принимает строку
    :param number: str
    :return: маску счета
    """
    logger.info("Принимаем номер счета: ")
    number_account = f"**{number[-4:]}"
    logger.info(f"Возвращаем маску счета: {number_account}")
    return number_account
