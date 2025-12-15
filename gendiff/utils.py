import json
import yaml

def load_data(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            elif file_path.endswith(('.yml', '.yaml')):
                return yaml.safe_load(f)
            else:
                print(f"Ошибка: неизвестный формат файла {file_path}.")
                return {}
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден.")
        return {}
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return {}

def generate_diff(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = []
    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if isinstance(val1, bool):
            val1 = str(val1).lower()
        if isinstance(val2, bool):
            val2 = str(val2).lower()

        if val1 == val2:
            result.append(f"    {key}: {val1}")
        else:
            if key in data1:
                result.append(f"- {key}: {val1}")
            if key in data2:
                result.append(f"+ {key}: {val2}")

    final_result = "{\n" + "\n".join(result) + "\n}"
    return final_result