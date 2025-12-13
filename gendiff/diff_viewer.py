def pretty_print_diff(diff_dict):
    lines = []
    for k, v in diff_dict.items():
        prefix = ''
        if k.startswith('+ ') or k.startswith('- '):
            prefix = k[:2].strip() + ' '
            k = k[2:]  
        lines.append(f'{prefix}{k}: {v}\n')
    return ''.join(lines)