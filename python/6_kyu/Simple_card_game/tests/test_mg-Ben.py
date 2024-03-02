import unittest


def compare_cards(card1, card2):
    # Create a priority list
    priority_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    # Check what is the card1's and card2's priority
    card1_priority = priority_list.index(card1)
    card2_priority = priority_list.index(card2)
    # Compare both priorities
    # Return result
    if card1_priority > card2_priority:
        return -1
    if card1_priority == card2_priority:
        return 0
    return 1


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
