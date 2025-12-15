import os
import unittest
from gendiff.generate_diff import generate_diff

class TestGenerateDiff(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file1_json = os.path.join(base_dir, '..', 'tests', 'test_data', 'file1.json')
        self.file2_json = os.path.join(base_dir, '..', 'tests', 'test_data', 'file2.json')
        self.file1_yaml = os.path.join(base_dir, '..', 'tests', 'test_data', 'file1.yml')
        self.file2_yaml = os.path.join(base_dir, '..', 'tests', 'test_data', 'file2.yml')

    def test_generate_diff_json(self):
        expected_output = (
            "{\n"
            "- follow: false\n"
            "  host: hexlet.io\n"
            "- proxy: 123.234.53.22\n"
            "- timeout: 50\n"
            "+ timeout: 20\n"
            "+ verbose: true\n"
            "}\n"
        )
        actual_output = generate_diff(self.file1_json, self.file2_json)
        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_generate_diff_yaml(self):
        expected_output = (
            "{\n"
            "- follow: false\n"
            "  host: hexlet.io\n"
            "- proxy: 123.234.53.22\n"
            "- timeout: 50\n"
            "+ timeout: 20\n"
            "+ verbose: true\n"
            "}\n"
        )
        actual_output = generate_diff(self.file1_yaml, self.file2_yaml)
        self.assertEqual(actual_output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()