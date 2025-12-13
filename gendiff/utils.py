import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None