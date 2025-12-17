SEPARATOR = " "
ADD_MARKER = "+ "
DELETE_MARKER = "- "
UNCHANGED_MARKER = "  "


def stylish_diff_formatter(diff, level_indent=2):
    indent = SEPARATOR * level_indent
    lines = []

    for entry in diff:
        key = entry["name"]
        act = entry["action"]
        val = format_value(entry.get("value"), level_indent)
        old_val = format_value(entry.get("old_value"), level_indent)
        new_val = format_value(entry.get("new_value"), level_indent)
        
        if act == "unchanged":       
            lines.append(f"{indent}{UNCHANGED_MARKER}{key}: {val}")
        elif act == "modified":      
            lines.append(f"{indent}{DELETE_MARKER}{key}: {old_val}")
            lines.append(f"{indent}{ADD_MARKER}{key}: {new_val}")
        elif act == "deleted":       
            lines.append(f"{indent}{DELETE_MARKER}{key}: {old_val}")
        elif act == "added":        
            lines.append(f"{indent}{ADD_MARKER}{key}: {new_val}")
        elif act == "nested":        
            nested_children = stylish_diff_formatter(entry.get("children"), level_indent+4)
            lines.append(f"{indent}{UNCHANGED_MARKER}{key}: {nested_children}")
            
    final_str = "\n".join(lines)
    end_indent = SEPARATOR * (level_indent - 2)
    return f"{{\n{final_str}\n{end_indent}}}"


def format_value(val, level_indent=2):
    if val is None:
        return "null"
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, dict):
        inner_indent = SEPARATOR * (level_indent + 4)
        result_lines = []
        for k, v in val.items():
            formated_v = format_value(v, level_indent + 4)
            result_lines.append(f"{inner_indent}{UNCHANGED_MARKER}{k}: {formated_v}")
        result_str = "\n".join(result_lines)
        end_indent = SEPARATOR * (level_indent + 2)
        return f"{{\n{result_str}\n{end_indent}}}"
    return str(val)


def format_diff_stylish(data):
    return stylish_diff_formatter(data)