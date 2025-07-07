def filter_by_state(list_of_operations: list, state: str = "EXECUTED") -> list:
    """Ищет в списке операции с определённым статусом"""
    result = []
    for data in list_of_operations:
        if data["state"] == state:
            result.append(data)
    return result


def sort_by_date(list_of_operations: list, is_reverse: bool = True) -> list:
    """Сортирует операции по дате"""
    result = sorted(list_of_operations, key=lambda x: x["date"], reverse=is_reverse)
    return result
