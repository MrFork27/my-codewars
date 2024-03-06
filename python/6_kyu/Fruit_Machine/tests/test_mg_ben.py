import unittest
import sys

sys.path.insert(0, "python/6_kyu/Fruit_Machine")

from mg_ben import fruit


class TestMgBen(unittest.TestCase):
    def setUp(self):
        self.reel1 = [
            "Wild",
            "Star",
            "Bell",
            "Shell",
            "Seven",
            "Cherry",
            "Bar",
            "King",
            "Queen",
            "Jack",
        ]
        self.reel2 = [
            "Bar",
            "Wild",
            "Queen",
            "Bell",
            "King",
            "Seven",
            "Cherry",
            "Jack",
            "Star",
            "Shell",
        ]
        self.reel3 = [
            "Bell",
            "King",
            "Wild",
            "Bar",
            "Seven",
            "Jack",
            "Shell",
            "Cherry",
            "Queen",
            "Star",
        ]
        self.reels = [self.reel1, self.reel2, self.reel3]

    def test_fruit(self):
        spin = [0, 1, 2]
        expected = 100
        self.assertEqual(fruit(self.reels, spin), expected, "fruit should return 100")

        spin = [5, 4, 3]
        expected = 0
        self.assertEqual(fruit(self.reels, spin), expected, "fruit should return 0")

        spin = [7, 0, 1]
        expected = 3
        self.assertEqual(fruit(self.reels, spin), expected, "fruit should return 3")

        spin = [7, 1, 1]
        expected = 6
        self.assertEqual(fruit(self.reels, spin), expected, "fruit should return 6")


if __name__ == "__main__":
    unittest.main()
