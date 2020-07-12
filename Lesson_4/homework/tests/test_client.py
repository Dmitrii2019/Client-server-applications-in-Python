import socket
import time
from unittest import TestCase

from Lesson_4.homework.client import create_presence, process_ans
from Lesson_4.homework.common.settings import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from Lesson_4.homework.common.utils import get_message, send_message


class ClientTestCase(TestCase):

    def setUp(self):
        self.account_name = 'Guest'
        self.message = {'response': 200}
        self.transport = socket.socket()
        self.transport.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.create_presence = {'action': 'presence', 'time': time.time(), 'user': {'account_name': 'Guest'}}
        send_message(self.transport, self.create_presence)

    def test_create_presence(self):
        data = create_presence(self.account_name)
        self.assertEqual(data, {'action': 'presence', 'time': time.time(), 'user': {'account_name': 'Guest'}})

    def test_process_ans(self):
        data = process_ans(self.message)
        self.assertEqual(data, '200 : OK')

    def test_main(self):
        data = process_ans(get_message(self.transport))
        self.assertEqual(data, '200 : OK')
