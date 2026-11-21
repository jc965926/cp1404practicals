class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


people = [Person("Mya", 22), Person("Mya", 22)]
print(people[0] == people[1])