import unittest
import main

class TestDay1(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(main.part_1("test.txt"), 142)


if __name__ == '__main__':
    unittest.main()