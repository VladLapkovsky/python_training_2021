"""This module provides one function to sort data from input file and write them to the output file.

Functions:
    names_sorter(path_to_input_file, path_to_output_file) -> file
"""


def sort(path_to_input_file, path_to_output_file):
    """Sort data from the input file and write them to the output file.

    Parameters:
        path_to_input_file: path to file with unsorted data.
        path_to_output_file: path to file with sorted data.

    """
    with open(path_to_input_file, "r") as input_file:
        with open(path_to_output_file, "w") as output_file:
            output_file.writelines(sorted(input_file))


if __name__ == "__main__":
    INPUT_FILE = "unsorted_names.txt"
    OUTPUT_FILE = "sorted_names.txt"
    sort(INPUT_FILE, OUTPUT_FILE)
