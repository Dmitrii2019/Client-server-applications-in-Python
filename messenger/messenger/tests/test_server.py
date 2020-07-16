import socket
from unittest import TestCase

from common.settings import (DEFAULT_IP_ADDRESS, DEFAULT_PORT, ERROR,
                             DEFAULT_IP_ADDRESS)
from common.utils import get_message, send_message
from server import process_client_message


class ServerTestCase(TestCase):

    def setUp(self):
        self.message_200 = {'action': 'presence', 'time': 1.1,
                            'user': {'account_name': 'Guest'}}
        self.message_400 = {'action': 'presence', 'time': 1.1,
                            'user': {'account_name': 'Person'}}

        self.transport = socket.socket()
        self.transport.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.create_presence = {'action': 'presence', 'time': 1.1,
                                'user': {'account_name': 'Guest'}}
        send_message(self.transport, self.create_presence)

    def test_process_client_message_200(self):
        data = process_client_message(self.message_200)
        self.assertEqual(data, {'response': 200})

    def test_process_client_message_400(self):
        data = process_client_message(self.message_400)
        self.assertEqual(data, {DEFAULT_IP_ADDRESS: 400, ERROR: 'Bad Request.'})

    def test_main(self):
        data = get_message(self.transport)
        self.assertEqual(data, {'response': 200})
