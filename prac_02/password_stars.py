MIN_PASSWORD_LENGTH=8

def main():
    """Get a valid password from user and display as asterisks"""
    password=get_valid_password()
    print_asterisks(password)

def get_valid_password():
    """Get valid password based on user input"""
    password = input("Enter your password: ")
    while len(password)<MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long. Please try again.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print password length as asterisks."""
    print('*' * len(password))

main()