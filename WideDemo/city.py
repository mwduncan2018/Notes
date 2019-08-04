#!/usr/bin/env python3
"""This is a demo for static typing in Python"""


class City:
    def __init__(self, name):
        self._name = name

    def get_crime_rate(self) -> str:
        if self._name == 'Baltimore':
            return 'Bad'
        else:
            return 'Ok'

    def get_mayor_name(self) -> str:
        if self._name == 'Baltimore':
            return "Martin O'Malley"
        else:
            return 'John Locke'


if __name__ == '__main__':
    pass