import json
import socket
import sys
import time

from homework.common.settings import (ACCOUNT_NAME, ACTION, DEFAULT_IP_ADDRESS,
                                      DEFAULT_PORT, ERROR, PRESENCE, RESPONSE, TIME, USER)
from homework.common.utils import get_message, send_message
from homework.log.client_log_config import LOG


def create_presence(account_name='Guest'):
    """Функция генерирует запрос о присутствии клиента."""
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """Функция разбирает ответ сервера."""
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    LOG.warning('Ошибка значения - не коректный ответ сервера ')
    raise ValueError


def main():
    """Загружаем параметы коммандной строки."""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        LOG.warning('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен.
    transport = socket.socket()
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        LOG.info(answer)
    except (ValueError, json.JSONDecodeError):
        LOG.warning('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()