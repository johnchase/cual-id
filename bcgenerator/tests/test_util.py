import unittest
from StringIO import StringIO
# from tempfile import NamedTemporaryFile, mkdtemp
from bcgenerator.util import (get_ids, get_x_y_coordinates,
                              get_barcodes)


class GetIds(unittest.TestCase):
    def setUp(self):
        self.id_file = StringIO(id_file)

    def test_get_ids(self):

        obs = get_ids(self.id_file)
        exp = ['Test_ID1', 'Test_ID2']
        self.assertEqual(obs, exp)

    def test_get_x_y_coordinates(self):
        columns = 2
        rows = 2
        x_start = 0
        y_start = 10
        obs = get_x_y_coordinates(columns, rows, x_start, y_start)
        exp = [(0.0, 28.346456692913389), (0.0, -52.214173228346468),
               (146.2677165354331, 28.346456692913389),
               (146.2677165354331, -52.214173228346468)]
        self.assertEqual(obs, exp)

    def test_get_barcodes(self):
        barcodes = get_barcodes(self.id_file, 'test_file')
        print barcodes
        self.assertTrue(barcodes.pageHasData)


id_file = """#SampleID
Test_ID1
Test_ID2"""

if __name__ == "__main__":
    unittest.main()
