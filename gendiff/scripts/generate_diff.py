from .diff_representation import DiffNode
from .utils import load_data
from ..formatters.stylish import render_stylish

def generate_diff(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)
    root = build_diff_tree(data1, data2)
    return render_stylish(root)

def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    root = DiffNode()
    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data1:
            node = DiffNode(key, None, val2, '+')
        elif key not in data2:
            node = DiffNode(key, val1, None, '-')
        elif val1 == val2:
            node = DiffNode(key, val1, val2, '=')
        elif isinstance(val1, dict) and isinstance(val2, dict):
            sub_root = build_diff_tree(val1, val2)
            node = DiffNode(key, val1, val2, '~', sub_root.children)
        else:
            node = DiffNode(key, val1, val2, '~')

        root.append_child(node)

    return root