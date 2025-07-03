from audioop import reverse


def filter_by_state(list_of_datas: list, state='EXECUTED') -> list:
    result = []
    for data in list_of_datas:
        if data['state'] == state:
            result.append(data)
    return result


def sort_by_date(list_of_datas: list, param_of_reverse=True) -> list:
    result = sorted(list_of_datas, key=lambda x: x['date'], reverse=param_of_reverse)
    return result
