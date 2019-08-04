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


def headline(text: str, city: City, align: bool = True) -> str:
    result = [text, city._name, ('Crime is ' + city.get_crime_rate())]
    if align:
        result.insert(0, 'aligned')
    return ' -- '.join(result)


if __name__ == '__main__':
    baltimore = City('Baltimore')
    print(headline('testing', baltimore, True))
