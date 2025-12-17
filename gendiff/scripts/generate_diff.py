from gendiff.formatters.format_id import format_id
from gendiff.scripts.find_diff import find_difference
from gendiff.scripts.parser import load_data_from_file


def generate_diff(file_path1, file_path2, formatter='stylish'):
    first_file_data = load_data_from_file(file_path1)
    second_file_data = load_data_from_file(file_path2)
    differences = find_difference(first_file_data, second_file_data)
    return format_id(differences, formatter)