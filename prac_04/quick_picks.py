"""
CP1404 Prac 4
Jamie Muirhead
Quick picks program
"""

from random import randint

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1

def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick.append(randint(MINIMUM, MAXIMUM))
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()


