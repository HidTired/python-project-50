import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument('file1', type=str, help="Path to the first config file")
    parser.add_argument('file2', type=str, help="Path to the second config file")
    parser.add_argument('-f', '--format', dest='fmt', choices=['plain', 'json'], default='plain',
                       help="Output format ('plain' or 'json')")

    args = parser.parse_args()
    diff = generate_diff(args.file1, args.file2)
    print(diff)

if __name__ == '__main__':
    main()