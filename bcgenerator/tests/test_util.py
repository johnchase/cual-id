import unittest
from StringIO import StringIO
from reportlab.lib.units import mm
from bcgenerator.util import get_ids, get_x_y_coordinates


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
        exp = [(0.0, 28.346456692913389),
               (0.0, -52.15748031496063),
               (147.96850393700791, 28.346456692913389),
               (147.96850393700791, -52.15748031496063)]
        self.assertEqual(obs, exp)

id_file = """#SampleID
Test_ID1
Test_ID2"""

if __name__ == "__main__":
    unittest.main()
