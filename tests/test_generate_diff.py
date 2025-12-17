from pathlib import Path
import unittest
from gendiff.generate_diff import generate_diff


class TestGenerateDiff(unittest.TestCase):
    def setUp(self):
        base_dir = Path(__file__).parent.resolve()
        self.file1_json = base_dir / 'test_data/file1.json'
        self.file2_json = base_dir / 'test_data/file2.json'
        self.file1_yaml = base_dir / 'test_data/file1.yml'
        self.file2_yaml = base_dir / 'test_data/file2.yml'
        self.pending_stylish = base_dir / 'test_data/pending_stylish'

    def test_generate_diff_flat_json(self):
        expected_output = self.pending_stylish.read_text().strip()
        actual_output = generate_diff(self.file1_json, self.file2_json)
        self.assertEqual(actual_output.strip(), expected_output)

    def test_generate_diff_flat_yaml(self):
        expected_output = self.pending_stylish.read_text().strip()
        actual_output = generate_diff(self.file1_yaml, self.file2_yaml)
        self.assertEqual(actual_output.strip(), expected_output)

    def test_generate_diff_nested_json(self):
        expected_output = self.pending_stylish.read_text().strip()
        actual_output = generate_diff(self.file1_json, self.file2_json)
        self.assertEqual(actual_output.strip(), expected_output)

    def test_generate_diff_nested_yaml(self):
        expected_output = self.pending_stylish.read_text().strip()
        actual_output = generate_diff(self.file1_yaml, self.file2_yaml)
        self.assertEqual(actual_output.strip(), expected_output)

if __name__ == "__main__":
    unittest.main()