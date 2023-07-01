from utils import main


def test_get_data_from_file(testdata_get_data_from_file__visualize_operations):
    assert main.get_data_from_file('test_get_data_from_file_1.json') == \
           testdata_get_data_from_file__visualize_operations
    assert main.get_data_from_file('test_get_data_from_file_2.json') == {}


def test_validate_data(testdata_validate_data_in, testdata_validate_data_out):
    assert main.validate_data(testdata_validate_data_in) == testdata_validate_data_out


def test_get_executed_operations(testdata_get_executed_operations_in, testdata_get_executed_operations_out):
    assert main.get_executed_operations(testdata_get_executed_operations_in) \
           == testdata_get_executed_operations_out


def test_sort_operations(testdata_sort_operations_in, testdata_sort_operations_out):
    assert main.sort_operations(testdata_sort_operations_in) == testdata_sort_operations_out


def test_visualize_operations(testdata_get_data_from_file__visualize_operations, capfd):
    main.visualize_operations(testdata_get_data_from_file__visualize_operations)
    out, err = capfd.readouterr()
    assert out == '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n\n'
