import unittest
from StringIO import StringIO
import pandas as pd

from barcode.util import get_ids


class GetIds(unittest.TestCase):
    def setUp(self):
        self.id_file = StringIO(id_file)

    def test_get_ids(self):
        sep = '\t'
        comment = None
        column = None
        obs = get_ids(self.id_file, comment, sep, column)
        exp = pd.Series(['Test_ID1', 'Test_ID2'])
        self.assertEqual(list(obs), list(exp))

id_file = """#SampleID
Test_ID1
Test_ID2"""

if __name__ == "__main__":
    unittest.main()
