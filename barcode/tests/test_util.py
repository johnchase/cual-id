import unittest
from StringIO import StringIO
import pandas as pd

from barcode.util import get_ids


class GetIds(unittest.TestCase):
    def setUp(self):
        self.id_file = StringIO(id_file)
        self.id_file2 = StringIO(id_file2)

    def test_get_ids(self):
        sep = '\t'
        comment = None
        column = None
        obs = get_ids(self.id_file, comment, sep, column)
        exp = pd.Series(['Test_ID1', 'Test_ID2'])
        self.assertEqual(list(obs), list(exp))

    def test_get_ids_with_comment(self):
        sep = '\t'
        comment = '#'
        column = None
        obs = get_ids(self.id_file2, comment, sep, column)
        exp = pd.Series(['Test_ID1', 'Test_ID2'])
        self.assertEqual(list(obs), list(exp))

id_file = """#SampleID
Test_ID1
Test_ID2"""

id_file2 = """#SampleID
##comment line
Test_ID1
Test_ID2"""

if __name__ == "__main__":
    unittest.main()
