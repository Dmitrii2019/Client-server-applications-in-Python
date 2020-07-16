import socket
import time
from unittest import TestCase

from common.settings import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message


class UtilsTestCase(TestCase):

    def setUp(self):
        self.transport = socket.socket()
        self.transport.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.create_presence = {'action': 'presence', 'time': time.time(), 'user': {'account_name': 'Guest'}}
        send_message(self.transport, self.create_presence)

    def test_get_message(self):
        data = get_message(self.transport)
        self.assertEqual(data, {'response': 200})
