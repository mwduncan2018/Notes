#!/usr/bin/env python3
"""This is a demo for static typing in Python"""

import unittest
from .test_cases import TestCases


class TestFlow(unittest.TestCase):

    test_cases = TestCases() # type: TestCases
    super_me = None # type: TestCases
    super_you = TestCases()

    def test_01_verify_a_web_socket_can_be_activated(self):
        self.test_cases.verify_a_web_socket_can_be_activated()

    def test_02_verify_a_web_socket_can_be_shut_down(self):
        self.test_cases.verify_a_web_socket_can_be_shut_down()

    def test_03_verify_a_web_socket_can_receive_a_message(self):
        self.test_cases.verify_a_web_socket_can_receive_a_message()




if __name__ == '__main__':
    unittest.main()