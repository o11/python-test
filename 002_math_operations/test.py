import unittest
from .math_operations import Math


class TestMath(unittest.TestCase):
    def setUp(self):
        self.math = Math(num_1=10, num_2=2)

    def test_init(self):
        self.assertEqual(self.math.num_1, 10)
        self.assertEqual(self.math.num_2, 2)

    def test_multiply(self):
        self.assertEqual(self.math.multiply(), 20)

    def test_division(self):
        self.assertEqual(self.math.division(), 5.0)

    def test_addition(self):
        self.assertEqual(self.math.addition(), 12)

    def test_subtraction(self):
        self.assertEqual(self.math.subtraction(), 8)

    def test_get_num_1(self):
        self.assertEqual(self.math.num_1, 10)

    def test_get_num_2(self):
        self.assertEqual(self.math.num_2, 2)

    def test_set_num_1(self):
        self.math.num_1 = 20
        self.assertEqual(self.math.num_1, 20)

    def test_set_num_2(self):
        self.math.num_2 = 3
        self.assertEqual(self.math.num_2, 3)


if __name__ == '__main__':
    unittest.main()
