MIN_LENGTH = 4
MAX_LENGTH = 10

def main():
    print("Please enter a valid password")
    print("YOur pass word must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    get_password()


def get_password():
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("*" * len(password))


def is_valid_password(password):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    for char in password:
        if char.isdigit():
            count_digit =+1
        elif char.islower():
            count_lower=+1
        elif char.isupper():
            count_upper =+1

        pass
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    return True

main()