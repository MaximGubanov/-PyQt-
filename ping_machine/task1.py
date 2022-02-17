"""Я выполнял код на Linux, поэтому есть отличеие в самой команде ping. К тому же я не смог реализовать запуск команды
посредством Popen, может быть на linux не хочет работать? И решил пойти по-другому пути: сделал запуск через
subprocess.run. В таком варианте у меня работает."""
from ipaddress import ip_address
from subprocess import PIPE
import subprocess
import socket


def get_ip(host_ip):
    """Ф-я преобразует строковое представление ip-адресса ("192.168.1.1") в объект ipaddress, если адрес представлен в виде
    доменного имени, то преобразует из домена в объект ipaddres.
    Пример:
        '192.168.1.1' <class 'str'>  ->  <class 'ipaddress.IPv4Address'>
        или
        'google.com' <class 'str'>  ->  <class 'ipaddress.IPv4Address'>
        или возвращает None, если неверный формат ip-адреса
    """
    try:
        return ip_address(host_ip)
    except ValueError:
        pass

    try:
        return ip_address(socket.gethostbyname_ex(host_ip)[2][0])
    except Exception:
        pass

    return None


def host_ping(ip_list):

    ip_address_list = {'REACHABLE': [], 'UNREACHABLE': []}

    for ip in ip_list:

        ip_addr = get_ip(ip)

        if ip_addr is None:
            print(f'"{ip}" - Неверный формат ip-адреса')
            continue

        proc_ping = subprocess.run(f'ping {ip_addr} -c 1', shell=True, stdout=PIPE)

        if proc_ping.returncode == 0:
            ip_address_list['REACHABLE'].append(ip_addr)
            print(f'{ip_addr} - узел доступен')
        else:
            ip_address_list['UNREACHABLE'].append(ip_addr)
            print(f'{ip_addr} - узел недоступен')

    return ip_address_list


if __name__ == '__main__':
    r = host_ping(
        ['google.com',
        '',
        '127.0.0.1',
        '192.168.1.100',
        'www.ya.ru',
        'http://mail.ru',
        'mail.ru']
    )
