def format_value(value):
    if isinstance(value, (dict, list)):   
        return '[сложное значение]'
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
    new_val = format_value(item.get('new_value'))
    old_val = format_value(item.get('old_value'))
    cur_path = f"{path}.{key}" if path else key

    ADD_MSG = f" была добавлена с значением: {new_val}"
    DEL_MSG = " была удалена"
    MOD_MSG = f" обновлено. Было: {old_val}, стало: {new_val}"
    NESTED_MSG = process_plain_diff(item.get('children'), cur_path)

    if action == 'added':
        return f"Свойство '{cur_path}'{ADD_MSG}"
    elif action == 'deleted':
        return f"Свойство '{cur_path}'{DEL_MSG}"
    elif action == 'modified':
        return f"Свойство '{cur_path}'{MOD_MSG}"
    elif action == 'nested':
        return NESTED_MSG
    return ''


def process_plain_diff(diff, path=''):
    results = []
    for item in diff:
        processed_item = process_plain_item(item, path)
        if processed_item:
            results.append(processed_item)
    return '\n'.join(results)


def format_diff_plain(diff):
    return process_plain_diff(diff)