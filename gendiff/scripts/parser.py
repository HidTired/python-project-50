import json
from pathlib import Path

import yaml


def determine_extension(file_path):
    ext = Path(file_path).suffix.lower()[1:]  
    return ext


def extract_file_contents(file_path):
    with open(file_path, encoding='utf-8') as file_obj:
        return file_obj.read()


def convert_to_data(content, ext):
    if ext == 'json':
        return json.loads(content)
    elif ext in ['yaml', 'yml']:
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Тип файла '{ext}' не поддерживается.")


def load_data_from_file(file_path):
    content = extract_file_contents(file_path)
    ext = determine_extension(file_path)
    return convert_to_data(content, ext)