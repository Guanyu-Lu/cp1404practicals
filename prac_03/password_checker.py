"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    display_requirements()
    password = get_valid_password()
    print(f"Your {len(password)}-character password is valid: {password}")

def display_requirements():
    """Display the requirements for this program."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

def get_valid_password():
    """Get valid password based on the requirements and user input"""
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    return password

def is_valid_password(password):
    """Determine if the provided password is valid."""
    number_of_lower, number_of_upper, number_of_digit, number_of_special=count_character_types(password)
    if not verify_number_of_character(number_of_lower):
        return False
    if not verify_number_of_character(number_of_upper):
        return False
    if not verify_number_of_character(number_of_digit):
        return False
    if check_number_of_special_character(number_of_special):
        return False
    if check_password_length(password):
        return False
    return True

def check_number_of_special_character(number_of_special):
    """Check whether number of special character satisfies the requirements."""
    return IS_SPECIAL_CHARACTER_REQUIRED and number_of_special < 1

def check_password_length(password):
    """Check if the password length is within the defined MIN and MAX limits."""
    return len(password) < MIN_LENGTH or len(password) > MAX_LENGTH

def count_character_types(password):
    """Count the number of character types and return numbers of lower, upper, digit, special characters."""
    counts = [0, 0, 0, 0] #index 0: lower, 1: upper, 2: digit, 3: special
    for character in password:
        if character.isdigit():
            counts[2] += 1
        elif character.isupper():
            counts[1] += 1
        elif character.islower():
            counts[0] += 1
        elif character in SPECIAL_CHARACTERS:
            counts[3] += 1
    number_of_lower = counts[0]
    number_of_upper = counts[1]
    number_of_digit = counts[2]
    number_of_special =counts[3]
    return number_of_lower,number_of_upper,number_of_digit,number_of_special

def verify_number_of_character(count):
    """Verify if the number of characters is more than zero."""
    return  count >= 1

main()