import unittest
from cualid.mint import (base10_to_base36, base36_to_base10,
                         encode, decode)


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
        exp = (26589444225832484022, '5M0IBBZ17246U')
        self.assertEqual(obs, exp)

    def test_decode(self):
        obs = decode(1236781)
        exp = 97549966513454363179
        self.assertEqual(obs, exp)

if __name__ == "__main__":
    unittest.main()
