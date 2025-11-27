import unittest


from Poker import isPair, isStraight, isThreeOfAKind


class TestPokerHands(unittest.TestCase): # erbt von unittest.TestCase

    def test_pair(self):
        hand = [
            ("2", "Herz"),
            ("2", "Karo"),
            ("5", "Pik"),
            ("7", "Kreuz"),
            ("9", "Herz")
        ]
        self.assertTrue(isPair(hand))

    def test_straight(self):
        hand = [
            ("6", "Herz"),
            ("7", "Karo"),
            ("8", "Pik"),
            ("9", "Kreuz"),
            ("10", "Herz")
        ]
        self.assertTrue(isStraight(hand))

    def test_three_of_a_kind(self):
        hand = [
            ("Bube", "Herz"),
            ("Bube", "Karo"),
            ("Bube", "Pik"),
            ("3", "Kreuz"),
            ("9", "Herz")
        ]
        self.assertTrue(isThreeOfAKind(hand))

    def test_wheel_straight(self):
        hand = [
            ("Ass", "Herz"),
            ("2", "Karo"),
            ("3", "Pik"),
            ("4", "Kreuz"),
            ("5", "Herz")
        ]
        self.assertTrue(isStraight(hand))

    def test_straight_false(self): # Methode die falsch schlägt
        hand = [
            ("10", "Herz"),
            ("2", "Karo"),
            ("3", "Pik"),
            ("4", "Kreuz"),
            ("5", "Herz")
        ]
        self.assertTrue(isStraight(hand))



if __name__ == "__main__":
    unittest.main()
