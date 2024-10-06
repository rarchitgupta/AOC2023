import unittest
import main

class TestDay1(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(main.part_1("test_part1.txt"), 142)


if __name__ == '__main__':
    unittest.main()