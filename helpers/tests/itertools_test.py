# testing
from unittest import TestCase

# helpers
from helpers.itertools import groupby


class TestItertools(TestCase):

    def test_groupby(self):
        iterable = [1, 3, 2, 3]
        got = {
            key: list(group)
            for key, group in groupby(iterable)
        }
        expected = {
            1: [1],
            2: [2],
            3: [3, 3],
        }
        self.assertEqual(expected, got)

        got = {
            key: list(group)
            for key, group in groupby(iterable, key=lambda x: x % 2)
        }
        expected = {
            0: [2],
            1: [1, 3, 3],
        }
        self.assertEqual(expected, got)
