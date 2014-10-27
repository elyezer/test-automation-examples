import unittest
import calculator
from ddt import ddt, data


@ddt
class CalculatorDDTTestCase(unittest.TestCase):
    @data(
        (40, 2, 42),
        (2, 2, 4),
        (20, 30, 50)
    )
    def test_add(self, test_data):
        a, b, c = test_data
        self.assertEqual(calculator.add(a, b), c)

    @data(
        (40, 2, 38),
        (2, 2, 0),
        (20, 30, -10)
    )
    def test_sub(self, test_data):
        a, b, c = test_data
        self.assertEqual(calculator.sub(a, b), c)
