import unittest
from solution import delete_nth


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            delete_nth([20, 37, 20, 21], 1),
            [20, 37, 21],
            "From list [20, 37, 20, 21], 1 you get",
        )

    def test_2(self):
        self.assertEqual(
            delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
            [1, 1, 3, 3, 7, 2, 2, 2],
            "From list [1, 1, 3, 3, 7, 2, 2, 2, 2], 3 you get",
        )

    def test_3(self):
        self.assertEqual(
            delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3),
            [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5],
            "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3 you get",
        )

    def test_4(self):
        self.assertEqual(
            delete_nth([1, 1, 1, 1, 1], 5),
            [1, 1, 1, 1, 1],
            "From list [1, 1, 1, 1, 1], 5 you get",
        )

    def test_5(self):
        self.assertEqual(delete_nth([], 5), [], "From list [], 5 you get")

    def test_6(self):
        self.assertEqual(
            delete_nth([12, 39, 19, 39, 39, 19, 12], 1),
            [12, 39, 19],
            "From list [12, 39, 19, 39, 39, 19, 12], 1 you get",
        )


if __name__ == '__main__':
    unittest.main()
