"""
Word Occurrences
Estimate: 25 minutes
Actual:   24 minutes
"""


def main():
    """Run the email-to-name dictionary program"""
    email_to_name = {}
    email = input("Email:").strip()
    while email != "":
        name = extract_name(email)
        name = confirm_name(name)
        email_to_name[name] = email
        email = input("Email:").strip()
    print()
    print_emails(email_to_name)


def confirm_name(name):
    """Confirm name based on the name from email"""
    confirmation = input(f"Is your name {name}? (Y/n)").upper()
    if confirmation == "N" or confirmation == "NO":
        name = input("Name:").strip()
    return name


def extract_name(email):
    """Exact name from email address"""
    name=email.split("@")[0]
    name=name.replace("."," ").replace("_", " ")
    return name.title()


def print_emails(email_to_name):
    """Print all names and emails"""
    for name,email in email_to_name.items():
        print(f"{name} ({email})")


main()




