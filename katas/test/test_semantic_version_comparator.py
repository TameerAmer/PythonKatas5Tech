import unittest
from katas.semantic_version_comparator import compare_versions

class TestSemanticVersionComparator(unittest.TestCase):

    def test_v1_newer(self):
        self.assertEqual(compare_versions('1.0.1', '1.0.0'), 1)
        self.assertEqual(compare_versions('2.0.0', '1.9.9'), 1)
        self.assertEqual(compare_versions('1.2.3', '1.2.2'), 1)
    
    def test_v2_newer(self):
        self.assertEqual(compare_versions('1.0.0', '1.0.1'), -1)
        self.assertEqual(compare_versions('1.9.9', '2.0.0'), -1)
        self.assertEqual(compare_versions('1.2.2', '1.2.3'), -1)

    def test_equal_versions(self):
        self.assertEqual(compare_versions('1.0.0', '1.0.0'), 0)
        self.assertEqual(compare_versions('2', '2.0.0'), 0)
        self.assertEqual(compare_versions('1.2.3', '1.2.3'), 0)
