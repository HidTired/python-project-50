from pathlib import Path
import json
import yaml

def load_data(filename):
    filename = Path(filename)
    try:
        if filename.is_file():
            if filename.suffix == '.json':
                with filename.open('r', encoding="utf-8") as f:
                    return json.load(f)
            elif filename.suffix == '.yaml' or filename.suffix == '.yml':
                with filename.open('r', encoding="utf-8") as f:
                    return yaml.safe_load(f)
            else:
                raise ValueError(f"Неизвестное расширение файла: {filename.suffix}")
        else:
            print(f"Ошибка: файл {filename} не найден.")
            return {}
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        return {}