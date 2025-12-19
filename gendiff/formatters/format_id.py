from .json import format_diff_json
from .plain import format_diff_plain
from .stylish import format_diff_stylish


def format_id(diff, formatter):
    match formatter:
        case 'stylish':
            return format_diff_stylish(diff)
        case 'plain':
            return format_diff_plain(diff)
        case 'json':
            return format_diff_json(diff)
        case _:
            raise ValueError(f"Unsupported file formatter '{formatter}'")