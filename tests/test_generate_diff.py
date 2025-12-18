import pytest

from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.parser import extract_file_contents


@pytest.mark.parametrize('file1,file2,expected', [
    ('tests/test_data/file1.json',
     'tests/test_data/file2.json',
     'tests/test_data/calculated_result_yaml.txt'),
    ('tests/test_data/file1.yml',
     'tests/test_data/file2.yml',
     'tests/test_data/calculated_result_yaml.txt'),
])
def test_generate_diff_styled(file1, file2, expected):
    diff = generate_diff(file1, file2)
    expected_output = extract_file_contents(expected).strip()
    assert diff.strip() == expected_output


@pytest.mark.parametrize('file1,file2,expected', [
    ('tests/test_data/file1.json',
    'tests/test_data/file2.json',
    'tests/test_data/calculated_result_plain.txt'),
    ('tests/test_data/file1.yml',
     'tests/test_data/file2.yml',
     'tests/test_data/calculated_result_plain.txt'),
])
def test_generate_diff_plain(file1, file2, expected):
    diff = generate_diff(file1, file2, formatter="plain")
    expected_output = extract_file_contents(expected).strip()
    assert diff.strip() == expected_output


@pytest.mark.parametrize('file1,file2,expected', [
    ('tests/test_data/file1.json',
    'tests/test_data/file2.json',
    'tests/test_data/calculated_result_json_format.txt'),
    ('tests/test_data/file1.yml',
     'tests/test_data/file2.yml',
     'tests/test_data/calculated_result_json_format.txt'),
])
def test_generate_diff_json(file1, file2, expected):
    diff = generate_diff(file1, file2, formatter="json")
    expected_output = extract_file_contents(expected).strip()
    assert diff.strip() == expected_output