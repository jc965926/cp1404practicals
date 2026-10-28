"""
Emails
Estimate: 25 minutes
Actual:   43 minutes
"""

email_to_name = {}
def main():
    new_email = input("Email: ")
    while new_email != "":
        new_name = get_name(new_email)
        name_check = input(f"Is your name {new_name}? (Y/n) ").upper()
        if name_check != "Y" and name_check != "":
            new_name = input("Name: ")
        email_to_name[new_email] = new_name
        new_email = input("Email: ")

    print("") # add blank line before listing names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    name_raw = email.split("@")[0]
    name_processed = " ".join([name.capitalize() for name in name_raw.split(".")])
    return name_processed

main()
