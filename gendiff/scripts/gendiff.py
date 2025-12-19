import argparse

from .generate_diff import generate_diff


def argument_parser():
    arg_pars = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference"
        )
    arg_pars.add_argument('first_file', help="The first file for comparison")
    arg_pars.add_argument('second_file', help="The second file for comparison")
    arg_pars.add_argument('-f', '--format',
                           choices=['stylish', 'plain', 'json'],
                            default='stylish',
                            help="set format of output")
    return arg_pars.parse_args()


def main():
    arguments = argument_parser()
    filepath_1 = arguments.first_file
    filepath_2 = arguments.second_file
    fmt = arguments.format
    comparison_result = generate_diff(filepath_1, filepath_2, fmt)
    print(comparison_result)


if __name__ == "__main__":
    main()