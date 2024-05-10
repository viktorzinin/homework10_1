from src.macks import get_mask_account, get_mask_card


def mask_account_card(number: str) -> str:
    """
    Функция принимает номер карты/счета
    :param number:str
    :return:маску карты/счета
    """
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card(number.split()[-1])
        result = f"{number[:-15]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """
    Функуия принимает строку с датой
    :param old_data: str
    :return:только дату
    """
    old_data_slice = old_data[:10]
    new_data = ".".join(old_data_slice.split("-")[::-1])
    return new_data
