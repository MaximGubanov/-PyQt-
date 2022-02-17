import ipaddress
from functools import reduce

from task1 import host_ping


def get_split_ip(ip):
    """Ф-я разбивает ip-адрес на две части и возвращает кортеж из двух элементов: строки и целого числа.
    Пример: '192.168.1.12' -> ('192.168.1', 12) """
    try:
        splited_ip = ip.split('.')
        last_oktet = splited_ip.pop(-1)
        splited_ip = reduce(lambda x, y: f'{x}.{y}', splited_ip)
        return (splited_ip, last_oktet)
    except ValueError:
        print('Неверный формат ip-адреса')
        return None


def host_range_ping(starting_ip, end_ip):
    """Ф-я принимает два параметра левого и правого диапозона ip-адресов и выводит их в конслоль в порядке очереди
    starting_ip - начальниый аргумент,
    end_ip - конечный аргумент,
    Пример:
        func('192.168.1.1', '192.168.1.4')
        Вывод в консоль:
        -> 192.168.1.1
        -> 192.168.1.2
        -> 192.168.1.3
        -> 192.168.1.4
    Примечание: ip1 должен быть меньше ip2
    """
    starting_address, start_oktet = get_split_ip(starting_ip)
    end_address, end_oktet = get_split_ip(end_ip)

    start = ipaddress.ip_address(f'{starting_address}.{start_oktet}')
    end = ipaddress.ip_address(f'{end_address}.{end_oktet}')

    if not starting_address == end_address:
        print('Подсеть ip-адресов не совпадает')
        exit()

    ip_address_list = [f'{starting_address}.{x}' for x in range(int(start_oktet), int(end_oktet) + 1) if start < end]

    if not len(ip_address_list) == 0:
        return host_ping(ip_address_list)
    else:
        print('Начальный аргумент диапозона должен быть меньше конечного.\n'
              'Задайте правильный порядок.')


if __name__ == '__main__':
    result_ping = host_range_ping('192.168.1.1', '192.168.1.5')