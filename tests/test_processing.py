import pytest
from homework.processing import filter_by_state, sort_by_date
from tests.conftest import list_for_tests


def test_filter_by_state(list_for_tests: list):
    assert filter_by_state(list_for_tests) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert filter_by_state(list_for_tests, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert filter_by_state([]) == []
    with pytest.raises(KeyError) as exc_info:
        filter_by_state([
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}
        ])
    assert str(exc_info.value) == "'Отсутствует информация о статусе операции'"


def test_sort_by_date(list_for_tests: list):
    assert sort_by_date(list_for_tests) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
    assert sort_by_date([]) == []
    with pytest.raises(KeyError) as exc_info:
        sort_by_date([
            {'id': 41428829, 'state': 'EXECUTED'},
            {'id': 939719570, 'state': 'EXECUTED'},
            {'id': 594226727, 'state': 'CANCELED'},
            {'id': 615064591, 'state': 'CANCELED'}
        ])
    assert str(exc_info.value) == "'Отсутствует информация о дате осуществления операции'"
