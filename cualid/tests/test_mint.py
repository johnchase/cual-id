import unittest
import itertools

from cualid import create_ids
from cualid.mint import within_d

class TestWithinD(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(within_d('12345', []))

    def test_single(self):
        self.assertTrue(within_d('12345', ['54321']))

    def test_hypercube(self):
        full = ['0000', '0111']
        all_possible = [''.join(e) for e in itertools.product('01', repeat=4)]

        for s in all_possible:
            self.assertFalse(within_d(s, full))

    def test_long(self):
        collection = ['abcdefghijk', 'a-c^efghijk', 'abcdef@h$jk']

        self.assertTrue(within_d('a_defghi_k', collection))
        self.assertTrue(within_d('abcd___hijk', collection))

        self.assertFalse(within_d('abc_efghijk', collection))
        self.assertFalse(within_d('abcdefghijk', collection))

if __name__ == "__main__":
    unittest.main()
