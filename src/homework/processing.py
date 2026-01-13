

def filter_by_state(list_of_operations: list, state: str = "EXECUTED") -> list:
    """Ищет в списке транзакции с определённым статусом."""
    result = []
    for data in list_of_operations:
        if 'state' not in data:
            raise KeyError("Отсутствует информация о состоянии транзакции")
        if data['state'] == state:
            result.append(data)
    return result


def sort_by_date(list_of_operations: list, is_reverse: bool = True) -> list:
    """Сортирует транзакции по дате."""
    for operation in list_of_operations:
        if 'date' not in operation:
            raise KeyError("Отсутствует информация о дате осуществления транзакции")
    result = sorted(list_of_operations, key=lambda x: x['date'], reverse=is_reverse)
    return result
