import unittest
from app import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        main.get_anime_by_slug()
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
