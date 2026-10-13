# def find_oldest_person(names, ages):
#     oldest_person_index = ages.index(max(ages))
#     return names[oldest_person_index]
#
# names = ["Gerald", "Rosetta", "Alex", "Lily"]
# ages = [34, 51, 16, 27]
#
# find_oldest_person(names, ages)

name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
new_name = input("Name: ")
new_age = int(input("Age: "))
name_to_age[new_name] = new_age
for name, age in name_to_age.items():
    print(f"{name} -{age:3}")