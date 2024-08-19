import unittest
from solution import order


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

    def test_2(self):
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")

    def test_3(self):
        self.assertEqual(order(""), "")


if __name__ == '__main__':
    unittest.main()
