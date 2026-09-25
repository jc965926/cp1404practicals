"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

def main():
    user_score = float(input("Enter score: "))
    user_rating = rate_score(user_score)
    print(f"User score {user_score:.1f} is {user_rating}")
    if user_rating == "Excellent":
        print("You get a prize!")

    random_score = randint(0, 100)
    random_rating = rate_score(random_score)
    print(f"Random: {random_score} = {random_rating}")

def rate_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()