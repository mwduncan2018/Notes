#!/usr/bin/env python3
"""This is a demo for static typing in Python"""

from city import City


def headline(text: str, city: City, align: bool = True) -> str:
    result = [text, city._name, ('Crime is ' + city.get_crime_rate())]
    if align:
        result.insert(0, 'aligned')
    return ' -- '.join(result)

def report(text, city: City, align=True):
    return "..."


if __name__ == '__main__':
    baltimore = City('Baltimore')
    print(headline('testing', baltimore, True))
