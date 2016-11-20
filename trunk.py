import unittest
import numpy as np

from test_case_with_storage import StorageTestCase


class Test(StorageTestCase):

    def test1(self):
        seq = np.random.choice(10, 5, False)
        fake_lookup = seq[0]
        self.assertIn(fake_lookup, seq)
        return list(seq)


if __name__ == '__main__':
    unittest.main()
