from gendiff.generate_diff import generate_diff

def test_flat_files_comparison():
    expected_output = '''\
- follow: False
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True'''

    actual_output = generate_diff('tests/files/file1.json', 'tests/files/file2.json')
    assert actual_output.strip() == expected_output.strip()