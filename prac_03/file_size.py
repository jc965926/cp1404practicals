def main():
    filename = input("Enter filename: ")
    while filename != "":
        try:
            print(f"{filename} has {determine_file_size(filename)} lines.")
            filename = input("Enter filename: ")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist")
            filename = input("Enter filename: ")

def determine_file_size(filename):
    number_of_lines = 0
    with open(filename) as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines

main()