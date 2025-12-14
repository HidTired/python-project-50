import json

def load_data(file_path: str) -> dict | None:
    def convert_boolean(dct):
        converted_dct = {}
        for key, value in dct.items():
            if isinstance(value, bool):
                converted_dct[key] = 'true' if value else 'false'
            else:
                converted_dct[key] = value
        return converted_dct

    try:
        with open(file_path, 'r') as f:
            data = json.load(f, object_hook=convert_boolean)
            print("Данные после загрузки:", data) 
            return data
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None