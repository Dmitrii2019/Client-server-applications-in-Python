import json
import socket
import sys

from Lesson_4.homework.common.settings import (ACCOUNT_NAME, ACTION,
                                               DEFAULT_PORT, ERROR,
                                               MAX_CONNECTIONS, PRESENCE,
                                               RESPONSE,
                                               RESPONSE_DEFAULT_IP_ADDRESS,
                                               TIME, USER)
from Lesson_4.homework.common.utils import get_message, send_message


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клинта.

    проверяет корректность, возвращает словарь-ответ для клиента.
    """
    if (
            ACTION in message and
            message[ACTION] == PRESENCE and
            TIME in message and
            USER in message and
            message[USER][ACCOUNT_NAME] == 'Guest'
    ):
        return {
            RESPONSE: 200
        }
    return {
        RESPONSE_DEFAULT_IP_ADDRESS: 400,
        ERROR: 'Bad Request.'
    }


def main():
    """
    Загрузка параметров командной строки.

    если нет параметров, то задаём значения по умоланию. server.py -a 127.0.0.1 -p 8888.
    """

    # Загружаем, какой адрес слушать.
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После параметра "a"- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Загружаем, на какой порт обращаться.
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра "-p" необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Готовим сокет
    transport = socket.socket()
    transport.bind((listen_address, listen_port))
    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
