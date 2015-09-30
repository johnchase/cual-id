import unittest
import itertools

from cualid import create_ids
from cualid.mint import greater_than_distance


class TestCreateIDS(unittest.TestCase):
    def test_create_ids(self):
        self.assertEqual(len(list(create_ids(10, 5))), 10)
        self.assertEqual(len(list(create_ids(0, 3))), 0)
        self.assertEqual(len(list(create_ids(1, 6))), 1)


class TestWithinD(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(greater_than_distance('12345', []))

    def test_single(self):
        self.assertTrue(greater_than_distance('12345', ['54321']))

    def test_hypercube(self):
        full = ['0000', '0111']
        all_possible = [''.join(e) for e in itertools.product('01', repeat=4)]

        for s in all_possible:
            self.assertFalse(greater_than_distance(s, full))

    def test_long(self):
        collection = ['abcdefghijk', 'a-c^efghijk', 'abcdef@h$jk']

        self.assertTrue(greater_than_distance('a_defghi_k', collection))
        self.assertTrue(greater_than_distance('abcd___hijk', collection))

        self.assertFalse(greater_than_distance('abc_efghijk', collection))
        self.assertFalse(greater_than_distance('abcdefghijk', collection))

if __name__ == "__main__":
    unittest.main()
