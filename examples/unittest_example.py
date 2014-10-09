import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(40, 2), 42)

    def test_sub(self):
        self.assertEqual(calculator.sub(40, 2), 38)

    def test_mul(self):
        self.assertEqual(calculator.mul(40, 2), 80)

    def test_div(self):
        self.assertEqual(calculator.div(40, 2), 20)

    def test_add_strings(self):
        self.assertEqual(calculator.add('a', 'b'), 'ab')

    def test_fail(self):
        self.assertEqual(calculator.sub(2, 4), 0)
