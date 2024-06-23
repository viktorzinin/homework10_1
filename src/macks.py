import logging

logging.basicConfig(
    filename="logs/application.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger()


def get_mask_card(number: str) -> str:
    """
    Функция принимает строку
    :param number:str
    :return: маску карты
    """
    logger.info(f"Принимаем номер карты: {number}")
    number_cards = f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    logger.info(f"Возвращаем маску карты: {number_cards}")
    return number_cards


def get_mask_account(number: str) -> str:
    """
    Функция принимает строку
    :param number: str
    :return: маску счета
    """
    logger.info(f"Принимаем номер счета: {number}")
    number_account = f"**{number[-4:]}"
    logger.info(f"Возвращаем маску счета: {number_account}")
    return number_account
