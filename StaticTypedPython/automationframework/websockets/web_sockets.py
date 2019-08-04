#!/usr/bin/env python3
"""This is a demo for static typing in Python"""

from typing import *

class WebSockets:

    def __init__(self):
        self._messages = [] # type: List[str]
        self._active = False # type: bool

    def activate(self) -> str:
        self._active = True
        return "Web Sockets Activated"

    def deactivate(self) -> str:
        self._active = False
        return "Web Sockets Deactivated"

    def receive_message(self, message: str) -> str:
        if self._active == True:
            self._messages.append(message)
            return message
        else:
            raise Exception()

    def write_messages(self) -> int:
        if self._active == True:
            f = open(r'C:/All_Python/zen_of_python/StaticTypedPython/TestResults/messages.txt', mode='wt',  encoding='utf-8')
            for message in self._messages:
                f.write(message + "\n")
            f.close()
            return len(self._messages)
        else:
            raise Exception()

    def read_messages(self) -> List[str]:
        if self._active == True:
            f = open(r'C:/All_Python/zen_of_python/StaticTypedPython/TestResults/messages.txt', mode='rt',  encoding='utf-8')
            self._messages = []
            for line in f.readlines():
                self._messages.append(line)
            f.close()
            return self._messages
        else:
            raise Exception()