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

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

max_name_length = max([len(pair[0]) for pair in data])
max_number_length = max([len(str(pair[1])) for pair in data])

print(max_name_length)
print(max_number_length)

for name, number in data:
    print(f"{name:<{max_name_length}} = {number:>{max_number_length}}")