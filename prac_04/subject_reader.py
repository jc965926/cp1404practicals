"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from operator import itemgetter

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    max_name_length = max([len(subject[1]) for subject in data])
    max_number_length = max([len(str(subject[2])) for subject in data])
    for i, subject in enumerate(data):
        print(f"{data[i][0]} is taught by {data[i][1]:<{max_name_length}} and has {data[i][2]:>{max_number_length}} students.")



def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        print(data)  # See if that worked

        subjects.append(data)
        print(subjects)
        print("----------")
    input_file.close()
    return subjects

main()