"""Утилиты."""

import json

from homework.common.settings import ENCODING, MAX_PACKAGE_LENGTH


def get_message(client):
    """
    Утилита приёма и декодирования сообщения.

    Принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку значения.
    : param client:
    : return: response
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения.

    Принимает словарь и отправляет его.
    : param sock:
    : param message:
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    assert type(encoded_message) == bytes
    sock.send(encoded_message)
