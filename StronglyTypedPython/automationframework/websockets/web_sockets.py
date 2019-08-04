import sys, os
import json

class WebSockets:

    def __init__(self):
        self._messages = [] # type: List[str]

    def activate(self) -> str:
        return "Web Sockets Activated"

    def deactivate(self) -> str:
        return "Web Sockets Deactivated"

    def receive_message(self, message: str) -> str:
        self._messages.append(message)
        return message

    def write_messages(self) -> int:
        f = open(r'C:/dev/Python/zen_of_python/TestResults/messages.txt', mode='wt',  encoding='utf-8')
        for message in self._messages:
            f.write(message + "\n")
        return len(self._messages)

    def read_messages(self) -> int:
        f = open(r'C:/dev/Python/zen_of_python/TestResults/messages.txt', mode='wt',  encoding='utf-8')
        self._messages = []
        for line in f.readlines():
            self._messages.append(line)
        return len(self._messages)