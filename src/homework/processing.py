from audioop import reverse


def filter_by_state(list_of_datas: list, state='EXECUTED') -> list:
    result = []
    for data in list_of_datas:
        if data['state'] == state:
            result.append(data)
    return result
