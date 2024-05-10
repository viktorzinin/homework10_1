def get_mask_card(number: str) -> str:
    """
    Функция принимает строку
    :param number:str
    :return: маску карты
    """
    number_cards = f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    return number_cards


def get_mask_account(number: str) -> str:
    """
    Функция принимает строку
    :param number: str
    :return: маску счета
    """
    number_account = f"**{number[-4:]}"
    return number_account
