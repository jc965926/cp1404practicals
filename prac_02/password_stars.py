MINIMUM_PASSWORD_LENGTH = 8

def main():
    user_password = get_password()
    print_stars(user_password)


def print_stars(user_password: str):
    print("*" * len(user_password))


def get_password() -> str:
    user_password = input("Enter a password: ")
    while len(user_password) < MINIMUM_PASSWORD_LENGTH:
        print("Password must be at least 8 characters long.")
        user_password = input("Enter a password: ")
    return user_password


main()
