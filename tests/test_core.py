import unittest

from farey_sequence_lib import farey_length, farey_sequence


class TestFareySequence(unittest.TestCase):
    def test_order_one(self):
        self.assertEqual(farey_sequence(1), [(0, 1), (1, 1)])

    def test_order_two(self):
        self.assertEqual(farey_sequence(2), [(0, 1), (1, 2), (1, 1)])

    def test_order_four(self):
        self.assertEqual(
            farey_sequence(4),
            [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)],
        )

    def test_order_five(self):
        self.assertEqual(
            farey_sequence(5),
            [
                (0, 1),
                (1, 5),
                (1, 4),
                (1, 3),
                (2, 5),
                (1, 2),
                (3, 5),
                (2, 3),
                (3, 4),
                (4, 5),
                (1, 1),
            ],
        )

    def test_zero_and_negative_are_empty(self):
        self.assertEqual(farey_sequence(0), [])
        self.assertEqual(farey_sequence(-3), [])

    def test_terms_are_reduced(self):
        from math import gcd

        for num, den in farey_sequence(20):
            self.assertEqual(gcd(num, den), 1, f"{num}/{den} is not reduced")

    def test_terms_are_sorted_and_in_range(self):
        seq = farey_sequence(12)
        values = [num / den for num, den in seq]
        self.assertEqual(values, sorted(values))
        self.assertTrue(all(0.0 <= v <= 1.0 for v in values))

    def test_endpoints(self):
        seq = farey_sequence(7)
        self.assertEqual(seq[0], (0, 1))
        self.assertEqual(seq[-1], (1, 1))

    def test_no_duplicate_fractions(self):
        seq = farey_sequence(15)
        self.assertEqual(len(seq), len(set(seq)))


class TestFareyLength(unittest.TestCase):
    def test_matches_sequence_length(self):
        for n in range(0, 30):
            self.assertEqual(farey_length(n), len(farey_sequence(n)), f"n={n}")

    def test_known_values(self):
        self.assertEqual(farey_length(1), 2)
        self.assertEqual(farey_length(2), 3)
        self.assertEqual(farey_length(3), 5)
        self.assertEqual(farey_length(4), 7)
        self.assertEqual(farey_length(5), 11)
        self.assertEqual(farey_length(6), 13)
        self.assertEqual(farey_length(7), 19)
        self.assertEqual(farey_length(8), 23)
        self.assertEqual(farey_length(9), 29)
        self.assertEqual(farey_length(10), 33)

    def test_non_positive(self):
        self.assertEqual(farey_length(0), 0)
        self.assertEqual(farey_length(-1), 0)


if __name__ == "__main__":
    unittest.main()
