def create_addition(key, value):
    return {'action': 'added', 'name': key, 'new_value': value}

def create_deletion(key, value):
    return {'action': 'deleted', 'name': key, 'old_value': value}

def create_no_change(key, value):
    return {'action': 'unchanged', 'name': key, 'value': value}

def create_modification(key, value1, value2):
    return {'action': 'modified', 'name': key, 'new_value': value2, 'old_value': value1}

def create_nesting(key, value1, value2):
    return {'action': 'nested', 'name': key, 'children': find_difference(value1, value2)}


def find_difference(data1, data2):
    all_keys = set(data1.keys()) | set(data2.keys())
    added_keys = set(data2.keys()) - set(data1.keys())
    deleted_keys = set(data1.keys()) - set(data2.keys())

    differences = []

    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key in added_keys:
            differences.append(create_addition(key, val2))
        elif key in deleted_keys:
            differences.append(create_deletion(key, val1))
        elif isinstance(val1, dict) and isinstance(val2, dict):
            differences.append(create_nesting(key, val1, val2))
        elif val1 != val2:
            differences.append(create_modification(key, val1, val2))
        else:
            differences.append(create_no_change(key, val1))


    sorted_differences = sorted(differences, key=lambda x: x['name'])

    return sorted_differences