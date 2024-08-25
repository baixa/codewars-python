import unittest
from solution import solution


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("helloWorld"), "hello World")
        self.assertEqual(solution("camelCase"), "camel Case")
        self.assertEqual(solution("breakCamelCase"), "break Camel Case")


if __name__ == '__main__':
    unittest.main()
