import json
import re
import pathlib


fixed_path = pathlib.Path.cwd().parent / 'operations' / 'operations.json'


def get_data_from_file(path: type or str) -> list or None:
    """
    :param path: Correct path based on location of where from the func was called to fetch banking transactions data
    :return: List of raw banking transactions data
    """
    with open(file=path, mode='r', encoding='utf-8') as file:
        return json.load(file)


def validate_data(data: list) -> list:
    """
    :param data: List of raw banking transactions data
    :return: List of valid transactions without missing data
    """
    for idx, entry in enumerate(data):
        if entry == {}:
            data.pop(idx)
    return data


def get_executed_operations(data: list) -> list:
    """
    :param data: List of valid banking transactions
    :return: List of transactions with executed operations based on 'state' key
    """
    executed_operations = list(filter(lambda entry: entry['state'] == 'EXECUTED', data))
    return executed_operations


def sort_operations(data: list) -> list:
    """
    :param data: List with executed transactions based on 'state' key
    :return: List sorted by date in descending order
    """
    sorted_by_date = sorted(data, key=lambda entry: entry['date'], reverse=True)
    return sorted_by_date


def visualize_operations(data: list) -> None:
    """
    :param data: Sorted list of executed transactions based on 'state' key
    :return: Nothing, prints 5 latest transactions
    """
    for entry in data[:5]:
        year, month, day = entry['date'].split('T')[0].split('-')
        from_info = entry.get('from', '')
        to_info = entry.get('to', '')
        # using Re to get corresponding 'from' and 'to' data about payment option and card/account number
        try:
            from_card_type = re.split(pattern='([0-9])', string=from_info)[0].strip()
            from_card_num = ''.join(re.split(pattern='([0-9])', string=from_info)[1:])
            to_card_type = re.split(pattern='([0-9])', string=to_info)[0].strip()
            to_card_num = ''.join(re.split(pattern='([0-9])', string=to_info)[1:])
        except TypeError:
            pass
        # prettifying the data, hiding full info with '*' and formatting it to be used in print statement
        if from_card_type != 'Счет':
            from_card_num = f'{from_card_num[:4]} ' \
                            f'{from_card_num[4:6]}** **** {from_card_num[-4:]}'
        else:
            from_card_num = f'**{from_card_num[-4:]}'

        if to_card_type != 'Счет':
            to_card_num = f'{to_card_num[:4]} ' \
                          f'{to_card_num[4:6]}** **** {to_card_num[-4:]}'
        else:
            to_card_num = f'**{to_card_num[-4:]}'

        sum_of_trans = entry.get('operationAmount', '').get('amount', '0')
        currency_of_trans = entry.get('operationAmount', '').get('currency', '').get('name', '')
        # Printing data in correct format based on the fact whether we have 'from' info or not and
        # whether out coming transaction was received on account or card
        if from_info == '':
            print(f'{day}.{month}.{year} {entry.get("description")}\n'
                  f'{to_card_type} {to_card_num}\n'
                  f'{sum_of_trans} {currency_of_trans}\n')
        elif from_card_type != 'Счет':
            print(f'{day}.{month}.{year} {entry.get("description")}\n'
                  f'{from_card_type} {from_card_num} -> '
                  f'{to_card_type} {to_card_num}\n'
                  f'{sum_of_trans} {currency_of_trans}\n')
        else:
            print(f'{day}.{month}.{year} {entry.get("description")}\n'
                  f'{from_card_type} {from_card_num} -> '
                  f'{to_card_type} {to_card_num}\n'
                  f'{sum_of_trans} {currency_of_trans}\n')


if __name__ == '__main__':
    visualize_operations(sort_operations(get_executed_operations(validate_data(get_data_from_file(fixed_path)))))
