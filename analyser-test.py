import unittest
from analyser import IosBuildInfo

class TestBuildInfo(unittest.TestCase):
    """
    Test class to test ``get_build_infos`` function
    """

    def test_all_values(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = 1 + 2
        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
