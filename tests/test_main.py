from utils import main


"""
Я наверное собрал все антипаттерны тестирования в одном файле
"""

def test_get_data_from_file():
    assert main.get_data_from_file('data_to_test_get_data_from_file_1.json') == [{
    "test id": 0,
    "test state": "FAILED",
    "test date": "32.12.1999",
    "test operationAmount": {
      "amount": "-99.43",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }}]
    assert main.get_data_from_file('data_to_test_get_data_from_file_2.json') == {}


def test_validate_data():
    assert main.validate_data(main.get_data_from_file('data_to_test_validate_data_1.json'))\
           == main.get_data_from_file('data_to_test_validate_data_2.json')


def test_get_executed_operations():
    assert main.get_executed_operations(main.get_data_from_file('data_to_test_get_executed_operations_1.json'))\
           == main.get_data_from_file('data_to_test_get_executed_operations_2.json')


def test_sort_operations():
    assert main.sort_operations(main.get_data_from_file('data_to_test_sort_operations_1.json'))\
           == (main.get_data_from_file('data_to_test_sort_operations_2.json'))


def test_visualize_operations(capfd):
    main.visualize_operations(main.get_data_from_file('data_to_visualize_operations.json'))
    out, err = capfd.readouterr()
    assert out == '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n\n'
