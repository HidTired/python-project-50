from typing import Optional
from .utils import load_data
from .diff_calculator import calculate_diff
from .diff_viewer import pretty_print_diff

def generate_diff(file_path1: str, file_path2: str) -> Optional[str]:
    try:
        old_data = load_data(file_path1)
        new_data = load_data(file_path2)

        if old_data is None or new_data is None:
            raise ValueError("Ошибка при чтении данных из файлов.")

        diff = calculate_diff(old_data, new_data)
        return pretty_print_diff(diff)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None