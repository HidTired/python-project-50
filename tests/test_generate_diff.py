import os
import unittest
from gendiff.diff_representation import DiffNode
from gendiff.utils import load_data
from gendiff.formatters.stylish import render_stylish
from gendiff.generate_diff import generate_diff

class TestGenerateDiff(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file1_json = os.path.join(base_dir, '..', 'tests', 'test_data', 'file1.json')
        self.file2_json = os.path.join(base_dir, '..', 'tests', 'test_data', 'file2.json')
        self.file1_yaml = os.path.join(base_dir, '..', 'tests', 'test_data', 'file1.yml')
        self.file2_yaml = os.path.join(base_dir, '..', 'tests', 'test_data', 'file2.yml')
        self.pending_stylish_txt = os.path.join(base_dir, '..', 'tests', 'test_data', 'pending_stylish.txt')

    def test_generate_diff_flat_json(self):
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

    def test_generate_diff_flat_yaml(self):
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

    def test_generate_diff_nested_json(self):
        # Читаем ожидаемый вывод из файла pending_stylish.txt
        with open(self.pending_stylish_txt, 'r') as f:
            expected_output = f.read().strip()
            
        # Выводим ожидаемый результат и реальный результат
        print("Expected output:")
        print(expected_output)
        print("\nActual output:")
        actual_output = generate_diff(self.file1_json, self.file2_json)
        print(actual_output)
        
        self.assertEqual(actual_output.strip(), expected_output)

    def test_generate_diff_nested_yaml(self):
        # Читаем ожидаемый вывод из файла pending_stylish.txt
        with open(self.pending_stylish_txt, 'r') as f:
            expected_output = f.read().strip()
            
        # Выводим ожидаемый результат и реальный результат
        print("Expected output:")
        print(expected_output)
        print("\nActual output:")
        actual_output = generate_diff(self.file1_yaml, self.file2_yaml)
        print(actual_output)
        
        self.assertEqual(actual_output.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()