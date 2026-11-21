"""
Jamie Muirhead
Time estimate for completion: 60 mins
Actual time: 60 mins
"""

import datetime

VINTAGE_AGE = 50
VINTAGE_STRING = "(vintage)"

class Guitar:
    def __init__(self, name="", year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        # Gibson L - 5 CES(1922): $16, 035.40
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        age = datetime.datetime.now().year - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age <= VINTAGE_AGE:
            return True
        else:
            return False

def main():
    print("My guitars!")
    guitars = list()
    name = " "
    while name != "":
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

    print("These are my guitars:")
    i = 0
    for guitar in guitars:
        i +=1
        if guitar.is_vintage():
            vintage_string = VINTAGE_STRING
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

main()