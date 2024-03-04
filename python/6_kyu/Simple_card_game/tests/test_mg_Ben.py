import unittest
import sys

# adding the current code to the system path
sys.path.insert(0, "python/6_kyu/Simple_card_game")

# importing the compare_cards
from mg_Ben import compare_cards


class TestMgBen(unittest.TestCase):
    def test_compare_cards(self):
        # Card1 is more priority than card2
        self.assertEqual(compare_cards("A", "3"), -1, "Compare cards should return -1")
        # Card1 is equally priority than card2
        self.assertEqual(compare_cards("5", "5"), 0, "Compare cards should return 0")
        # Card1 is less priority than card2
        self.assertEqual(compare_cards("5", "J"), 1, "Compare cards should return 1")


if __name__ == "__main__":
    unittest.main()
