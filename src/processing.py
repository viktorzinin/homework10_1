def get_sorted(list_dict: list, state: str = "EXECUTED") -> list:
    """Функуия фильтрует список словарей по ключу state"""
    filter_list = []
    for ld in list_dict:
        if ld.get("state") == state:
            filter_list.append(ld)
    return filter_list


def get_date_sorted(list_dict: list, direction: bool = True) -> list:
    """Функция сортирует по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
