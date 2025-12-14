from typing import Dict, Set, Any

def calculate_diff(old_data: Dict[str, Any], new_data: Dict[str, Any]) -> Dict[str, Any]:
    diff_result = {}
    all_keys = set(old_data.keys()).union(new_data.keys())

    for key in sorted(all_keys):
        old_value = old_data.get(key)
        new_value = new_data.get(key)

        if old_value == new_value:
            diff_result[key] = old_value
        elif old_value is None:
            diff_result[f"+ {key}"] = new_value
        elif new_value is None:
            diff_result[f"- {key}"] = old_value
        else:
            diff_result[f"- {key}"] = old_value
            diff_result[f"+ {key}"] = new_value

    return diff_result