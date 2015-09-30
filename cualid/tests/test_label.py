import unittest
from io import StringIO
from cualid.label import (get_x_y_coordinates, get_barcodes)


class GetIds(unittest.TestCase):
    def setUp(self):
        self.id_file = StringIO(id_file)

    def test_get_x_y_coordinates(self):
        columns = 2
        rows = 2
        x_start = 0
        y_start = 10
        obs = get_x_y_coordinates(columns, rows, x_start, y_start)
        exp = [(0.0, 28.346456692913389), (0.0, -52.214173228346468),
               (146.2677165354331, 28.346456692913389),
               (146.2677165354331, -52.214173228346468)]
        self.assertEqual(list(obs), exp)

    def test_get_barcodes(self):
        barcodes = get_barcodes(self.id_file, 'test_file', suppress_ids=False)
        self.assertTrue(barcodes.pageHasData)


id_file = """8f648a23-9975-4af9-98fe-5df4eb98da0e	eb98da0e
c7545b8a-fcf2-484e-846b-2c7acde1179c	cde1179c
"""

if __name__ == "__main__":
    unittest.main()
