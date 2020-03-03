import unittest
import pytest
from simpleCalculatorr import simplecalculator


class test_Calculator(unittest.TestCase):
    def test_calc(self):
        assert simplecalculator

    def test_calc_add(self):
        assert simplecalculator.add(3, 2) == 5

    def test_calc_subtract(self):
        assert simplecalculator.subtract(0, 10) == -10

    def test_calc_multiply(self):
        assert simplecalculator.multiply(2, 2) == 4

    def test_calc_divide(self):
        assert simplecalculator.divide(10, 5) == 2

    def test_calc_square(self):
        assert simplecalculator.square(4) == 16

    def test_calc_sqrt(self):

        assert simplecalculator.sqrt(4) == 2
