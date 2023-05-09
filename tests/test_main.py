from utils import main


def test_get_data_from_file(data_to_test_get_data_from_file__to_test_visualize_operations):
    assert main.get_data_from_file('data_to_test_get_data_from_file_1.json') ==\
           data_to_test_get_data_from_file__to_test_visualize_operations
    assert main.get_data_from_file('data_to_test_get_data_from_file_2.json') == {}


def test_validate_data(data_to_test_validate_data_in, data_to_test_validate_data_out):
    assert main.validate_data(data_to_test_validate_data_in) == data_to_test_validate_data_out


def test_get_executed_operations(data_to_test_get_executed_operations_in, data_to_test_get_executed_operations_out):
    assert main.get_executed_operations(data_to_test_get_executed_operations_in) \
           == data_to_test_get_executed_operations_out


def test_sort_operations(data_to_test_sort_operations_in, data_to_test_sort_operations_out):
    assert main.sort_operations(data_to_test_sort_operations_in) == data_to_test_sort_operations_out


def test_visualize_operations(data_to_test_get_data_from_file__to_test_visualize_operations, capfd):
    main.visualize_operations(data_to_test_get_data_from_file__to_test_visualize_operations)
    out, err = capfd.readouterr()
    assert out == '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n\n'
