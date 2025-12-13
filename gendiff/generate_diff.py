from .utils import load_data
from .diff_calculator import calculate_diff
from .diff_viewer import pretty_print_diff

def generate_diff(file_path1, file_path2):
    old_data = load_data(file_path1)
    new_data = load_data(file_path2)
    
    if old_data is None or new_data is None:
        return None
    
    diff = calculate_diff(old_data, new_data)
    return pretty_print_diff(diff)