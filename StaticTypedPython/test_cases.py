#!/usr/bin/env python3
"""This is a demo for static typing in Python"""

from automationframework.websockets.web_sockets import WebSockets

class TestCases:

    def __init__(self):
        self._web_sockets = None # type: WebSockets

    def verify_a_web_socket_can_be_activated(self):
        self._web_sockets = WebSockets()
        result = self._web_sockets.activate()
        assert result == 'Web Sockets Activated'
        self._web_sockets.deactivate()

    def verify_a_web_socket_can_be_shut_down(self):
        self._web_sockets = WebSockets()
        self._web_sockets.activate()
        result = self._web_sockets.deactivate()
        assert result == 'Web Sockets Deactivated'

    def verify_a_web_socket_can_receive_a_message(self):
        self._web_sockets = WebSockets()
        self._web_sockets.activate()
        test_str = 'Why I have believed as many as seven things before breakfast'
        result = self._web_sockets.receive_message(test_str)
        assert result == test_str
        assert self._web_sockets._messages[0] == test_str

    def verify_a_web_socket_can_write_a_message(self):
        self._web_sockets = WebSockets()
        self._web_sockets.activate()
        self._web_sockets.receive_message('Four score and seven years ago')
        self._web_sockets.write_messages()
        result = self._web_sockets.read_messages()


