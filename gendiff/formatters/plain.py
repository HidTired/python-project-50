def format_value(value):
    if isinstance(value, (dict, list)):   
        return '[complex value]'
    elif value is None:                   
        return 'null'
    elif isinstance(value, bool):         
        return str(value).lower()
    elif isinstance(value, str):          
        return f"'{value}'"
    else:                                
        return str(value)


def process_plain_item(item, path=''):
    key = item.get('name')
    action = item.get('action')
    cur_path = f"{path}.{key}" if path else key

    if action == 'nested':
        children = item.get('children') or []
        return process_plain_diff(children, cur_path)

    new_val = format_value(item.get('new_value'))
    old_val = format_value(item.get('old_value'))

    if action == 'added':
        return f"Property '{cur_path}' was added with value: {new_val}"
    elif action == 'deleted':
        return f"Property '{cur_path}' was removed"
    elif action == 'modified':
        return (f"Property '{cur_path}' was updated. "
                f"From {old_val} to {new_val}")
    return ''


def process_plain_diff(diff, path=''):
    if not diff:
        return ''
    results = []
    for item in diff:
        processed_item = process_plain_item(item, path)
        if processed_item:
            results.append(processed_item)
    return '\n'.join(results)


def format_diff_plain(diff):
    return process_plain_diff(diff)