import unittest
from StringIO import StringIO

from barcode.util import get_barcode_ids


class GetBarcodeIds(unittest.TestCase):
    def setUp(self):
        self.id_file = StringIO(id_file)

    def test_get_barcode_ids(self):
        obs = get_barcode_ids(self.id_file, '#')
        exp = ['TestID1, Test_ID2']
        self.assertEqual(obs, exp)

id_file = "#SampleID    Test_ID1    Test_ID2"

if __name__ == "__main__":
    unittest.main()
