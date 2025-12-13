from gendiff.utils import load_data

file_paths = ['file1.json', 'file2.json']
for path in file_paths:
    data = load_data(path)
    if data:
        print(f"Содержимое файла '{path}':")
        print(data)
    else:
        print(f"Не удалось прочитать файл '{path}'.")