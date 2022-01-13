"""
Classes to test pytest
"""
import json
import numbers


class MysteryError(Exception):
    pass


def add(a, b):
    if a == 99:
        raise MysteryError()
    return a + b


def read_json(some_file):
    with open(some_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class CalculatorError(Exception):
    """ Custom Exception """
    pass


class Calculator:
    """
    A calculator
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, x, y):
        self._check_operand(x)
        self._check_operand(y)
        return x + y

    def subtract(self):
        return self.x - self.y

    @staticmethod
    def _check_operand(operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'{operand} is not a number')
