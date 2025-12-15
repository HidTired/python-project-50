from .utils import load_data
def generate_diff(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = []
    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if val1 == val2:
            result.append(f"    {key}: {val1}")
        else:
            if key in data1:
                result.append(f"- {key}: {val1}")
            if key in data2:
                result.append(f"+ {key}: {val2}")

    final_result = "{\n" + "\n".join(result) + "\n}"
    return final_result