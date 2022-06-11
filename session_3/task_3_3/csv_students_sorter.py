"""CSV students data sorter.

A simple CSV sorter provides two function to receive data from CSV file and sort them according to the functions.

CSV file should contain next headers:
student name,age,average mark

Functions:
    get_top_performers(file_path, number_of_top_students=5):
        get top students from CSV file and sort them by average mark.
    write_to_csv_by_age(file_path):
        write sorted-by-age information about students from/to the CSV file.
"""


import csv


def get_top_performers(file_path, number_of_top_students=5):
    """Get top students from CSV file and sort them by average mark.

    Parameters:
        file_path: path to the CSV file with unsorted students.
        number_of_top_students: number of top performer students in result list.

    Returns:
        A list of top performer students like -> ["name", "name", "name", ].
    """
    with open(file_path) as file_to_read:
        reader = csv.DictReader(file_to_read)

        # sorting students by "average mark", top first and getting list like:
        # [{"student name": "name", "age": "age", "average mark": "mark"}]:
        sorted_students = sorted(
            reader,
            key=lambda dicts: float(dicts["average mark"]),
            reverse=True,
        )
        return [name["student name"] for name in sorted_students[:number_of_top_students]]


def write_to_csv_by_age(file_path):
    """Write sorted-by-age information about students from/to the CSV file.

    Receive the file path with students info and write CSV student information
    to the new file in descending order of age.

    Create new file named like -> "sorted_{file_path}".
    If the file does not exist, a new one will be created.
    If the file exists, it"s will be rewritten.

    CSV structure in resulting file:
        Headers:
            student name,age,average mark

        Items:
            Name,max_age,mark
            Name,max_age,mark
            ...

    Parameters:
        file_path: path to the CSV file with unsorted students.
    """
    with open(file_path, "r") as file_to_read:
        with open(f"sorted_{file_path}", "w", newline="") as file_to_write:
            reader = csv.DictReader(file_to_read)

            # sorting students by "age", top first and getting list like:
            # [{"student name": "name", "age": "age", "average mark": "mark"}]:
            sorted_students = sorted(
                reader,
                key=lambda dicts: float(dicts["age"]),
                reverse=True,
            )
            writer = csv.DictWriter(
                file_to_write,
                fieldnames=sorted_students[0].keys(),
            )
            writer.writeheader()
            writer.writerows(sorted_students)


def main():
    """Print names of top performer students and writes student info to the new CSV file in descending order of age."""
    print(get_top_performers("students.csv", 5))
    write_to_csv_by_age("students.csv")


if __name__ == "__main__":
    main()
