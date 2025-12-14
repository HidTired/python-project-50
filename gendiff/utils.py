import json

def load_data(file_path: str) -> dict | None:
    """
    Загружает данные из JSON-файла, с дополнительным контролем булевых значений.

    :param file_path: Путь к файлу
    :return: Словарь с данными или None в случае ошибки
    """
    def convert_boolean(dct):
        """
        Хук-преобразователь, позволяющий поменять булевые значения на строки.
        """
        converted_dct = {}
        for key, value in dct.items():
            if isinstance(value, bool):
                converted_dct[key] = 'true' if value else 'false'
            else:
                converted_dct[key] = value
        return converted_dct

    try:
        with open(file_path, 'r') as f:
            # Читаем данные с преобразованием булевых значений
            data = json.load(f, object_hook=convert_boolean)
            print("Данные после загрузки:", data)  # Diagnostic output
            return data
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None