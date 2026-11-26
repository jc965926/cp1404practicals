name = input("Name: ")
vowels = ["a", "e", "i", "o", "u"]
number_of_vowels = 0
number_of_characters = len(name)
for letter in name:
    if letter in vowels:
        number_of_vowels += 1
print(f"Out of {number_of_characters} characters, {name} has {number_of_vowels} vowels")