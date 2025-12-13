from gendiff.generate_diff import generate_diff
import argparse

def main():
    parser = argparse.ArgumentParser(description='Compare two configuration files.')
    parser.add_argument('file1', help='Path to the first config file')
    parser.add_argument('file2', help='Path to the second config file')
    args = parser.parse_args()

    diff_result = generate_diff(args.file1, args.file2)
    if diff_result is not None:
        print(diff_result)
    else:
        print("Ошибка при обработке файлов.")

if __name__ == '__main__':
    main()