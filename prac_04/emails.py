"""
Word Occurrences
Estimate: 25 minutes
Actual:   ?? minutes
"""

email_to_name = {}
def main():
    new_email = input("Email: ")
    while new_email != "":
        new_name = get_name(new_email)
        print(new_name)
        new_email = input("Email: ")

def get_name(email):
    name_raw = email.split("@")[0]
    name_processed = " ".join([name.capitalize() for name in name_raw.split(".")])
    return name_processed

main()
