# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove? ")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#         print(", ".join(names))
#     except ValueError:
#         print(f"'{name_to_remove}' not in list")
#     name_to_remove = input("Who do you want to remove? ")
# print("Finished.")

# numbers
# number_of_people
# age
# coordinates
# is_mutant
# index

# should use read the file line-by-line, with a for loop and readline()
# sum_of_numbers should be called total for consistency with problem domain
# naming is misleading, as numbers is a string. could use line instead

from operator import itemgetter

name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

name_width = max(len(name) for name in name_to_score)
number_width = max(len(name_to_score) for name in name_to_score)

print(name_width)
print(number_width)

for name, score in name_to_score.items():
    print(f"{name:<{name_width}} = {score:>{number_width}}")