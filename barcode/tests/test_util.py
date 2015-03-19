import unittest
from StringIO import StringIO

from barcode.util import get_ids, get_x_y_coordinates


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
        exp = [(0.0, 720.0),
               (0.0, 632.87999999999988),
               (158.40000000000001, 720.0),
               (158.40000000000001, 632.87999999999988)]
        self.assertEqual(obs, exp)

id_file = """#SampleID
Test_ID1
Test_ID2"""

if __name__ == "__main__":
    unittest.main()
