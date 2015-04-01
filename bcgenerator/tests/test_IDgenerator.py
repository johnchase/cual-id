import unittest
from bcgenerator.IDgenerator import (base10_to_base36, base36_to_base10,
                                     encode, decode, get_mapping_file)


class IDGenerator(unittest.TestCase):
    # def setUp(self):

    def test_base10_to_base36(self):
        obs = base10_to_base36(10)
        exp = 'A'
        self.assertEqual(obs, exp)

    def test_base10_to_base36_negative(self):
        obs = base10_to_base36(-10)
        exp = '-A'
        self.assertEqual(obs, exp)

    def test_base10_to_base36_rasises_value_error(self):
        with self.assertRaises(TypeError):
            base10_to_base36('foo')

    def test_base36_to_base10(self):
        obs = base36_to_base10('A')
        exp = 10
        self.assertEqual(obs, exp)

    def test_encode(self):
        obs = encode(999999)
        exp = (51253930955819896761L, 'ATEIQ6KK5O0XL')
        self.assertEqual(obs, exp)

    def test_decode(self):
        obs = decode(1236781)
        exp = 97549966513454363179L
        self.assertEqual(obs, exp)

    def test_get_mapping_file(self):
        obs = len(get_mapping_file(10).split())
        exp = 11
        self.assertEqual(obs, exp)

if __name__ == "__main__":
    unittest.main()
