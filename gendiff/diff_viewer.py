from typing import Dict, Any

def pretty_print_diff(diff_dict: Dict[str, Any]) -> str:
    lines = [] 

    lines.append('{\n')


    for k, v in diff_dict.items():
        prefix = '' 
        if k.startswith('+ ') or k.startswith('- '):
            prefix = k[:2].strip()
            k = k[2:]
        

        if isinstance(v, bool):
            v = 'true' if v else 'false'
        
        lines.append(f'{" ":3}{prefix} {k}: {v}\n')

    lines.append('}')

    return ''.join(lines)