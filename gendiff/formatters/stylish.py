def render_stylish(diff, indent=0):
    lines = []
    spaces = ' ' * indent

    for key, info in diff.items():
        typ = info['type']
        if typ == 'added':
            lines.append(f'{spaces}+ {key}: {format_value(info["new_value"], indent)}')
        elif typ == 'deleted':
            lines.append(f'{spaces}- {key}: {format_value(info["old_value"], indent)}')
        elif typ == 'changed':
            lines.extend([
                f'{spaces}- {key}: {format_value(info["old_value"], indent)}',
                f'{spaces}+ {key}: {format_value(info["new_value"], indent)}'
            ])
        elif typ == 'nested':
            nested_block = render_stylish(info['children'], indent + 4)
            lines.append(f'{spaces}{key}: {{')
            lines.extend(nested_block.split('\n'))
            lines.append(f'{spaces}}}')
        else: 
            lines.append(f'{spaces}  {key}: {format_value(info["old_value"], indent)}')

    return '\n'.join(lines)

def format_value(value, indent):
    if isinstance(value, dict):
        return render_stylish(value, indent + 4)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return repr(value)[1:-1]