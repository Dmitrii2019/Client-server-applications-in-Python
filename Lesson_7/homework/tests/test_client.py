import socket
from unittest import TestCase

from client import create_presence, process_ans
from common.settings import DEFAULT_IP_ADDRESS, DEFAULT_PORT, PRESENCE, TIME, USER, ACCOUNT_NAME, ACTION
from common.utils import get_message, send_message


class ClientTestCase(TestCase):

    def setUp(self):
        self.account_name = 'Guest'
        self.message = {'response': 200}
        self.transport = socket.socket()
        self.transport.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.create_presence = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
        send_message(self.transport, self.create_presence)

    def test_create_presence(self):
        data = create_presence(self.account_name)
        data[TIME] = 1.1  # время необходимо приравнять принудительно
        self.assertEqual(data, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_process_ans(self):
        data = process_ans(self.message)
        self.assertEqual(data, '200 : OK')

    def test_main(self):
        data = process_ans(get_message(self.transport))
        self.assertEqual(data, '200 : OK')
