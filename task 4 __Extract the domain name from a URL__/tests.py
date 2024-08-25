import unittest
from solution import domain_name


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("https://123.net"), "123")
        self.assertEqual(domain_name("https://hyphen-site.org"), "hyphen-site")
        self.assertEqual(domain_name("http://codewars.com"), "codewars")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("http://www.codewars.com/kata/"), "codewars")
        self.assertEqual(domain_name("icann.org"), "icann")


if __name__ == '__main__':
    unittest.main()
