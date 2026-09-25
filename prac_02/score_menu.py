"""
CP1404 - Practical
Program to ???
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = float(input("Enter score: "))
    rating = rate_score(score)
    while rating == "Invalid":
        print("Invalid score")
        score = float(input("Enter score: "))
        rating = rate_score(score)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            rating = rate_score(score)
            while rating == "Invalid":
                print("Invalid score")
                score = float(input("Enter score: "))
                rating = rate_score(score)
        elif choice == "P":
            print(f"Your score {score:.1f} is {rating}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")

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