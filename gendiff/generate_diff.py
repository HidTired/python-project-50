from scripts.utils import load_data
from formatters.stylish import render_stylish

def generate_diff(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)
    root = build_diff_tree(data1, data2)
    return render_stylish(root)

def build_diff_tree(data1, data2):
    diff = {}
    all_keys = set(data1.keys()).union(data2.keys())
    
    for key in all_keys:
        if key not in data1:
            diff[key] = {'type': 'added', 'new_value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'old_value': data1[key]}
        elif data1[key] != data2[key]:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                nested_diff = build_diff_tree(data1[key], data2[key])
                diff[key] = {'type': 'nested', 'children': nested_diff}
            else:
                diff[key] = {'type': 'changed', 'old_value': data1[key], 'new_value': data2[key]}
        else:
            diff[key] = {'type': 'unchanged'}
            
    return diff