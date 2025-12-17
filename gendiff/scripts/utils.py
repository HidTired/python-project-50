from pathlib import Path
import json
import yaml

def load_data(filename):
    filename = Path(filename) 
    if filename.is_file():
        ext = filename.suffix.lower()
        if ext == '.json':
            with filename.open('r', encoding="utf-8") as f:
                return json.load(f)
        elif ext == '.yaml' or ext == '.yml':
            with filename.open('r', encoding="utf-8") as f:
                return yaml.safe_load(f)
        else:
            raise ValueError(f"Неизвестное расширение файла: {ext}")
    else:
        print(f"Ошибка: файл {filename} не найден.")
        return {}