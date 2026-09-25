user_name = input("Enter name: ")
key_choice = " "

while key_choice[0] != "Q":
    print("(H)ello \n(G)oodbye \n(Q)uit")
    key_choice = input("Press a key to choose: ").upper()
    if key_choice[0] == "H":
        print(f"Hello {user_name}")
    elif key_choice[0] == "G":
        print(f"Goodbye {user_name}")
    elif key_choice[0] == "Q":
        pass
    else:
        print("Invalid choice")

print("Finished.")