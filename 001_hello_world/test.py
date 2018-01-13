import unittest

from .hello_world import say_hello_world


class TestSayHelloWorld(unittest.TestCase):
    def test_say_hello_world(self):
        self.assertEqual(say_hello_world(), 'Hello World')


if __name__ == '__main__':
    unittest.main()
