# Generate pseudo-random numbers
import secrets

# Common string operations
import string

# Defines what characters to use in generated passwords.
# String of ASCII characters which are considered printable.
# This is a combination of digits, ascii_letters, punctuation, and whitespace.
characters = string.ascii_letters + string.digits + string.punctuation

# Defines total number of passwords requested
number = int(input("How many passwords? "))

# Defines length of passwords
length = int(input("Password length: "))

# Calls number variable
for i in range(number):
    # What the password will be
    password = ''
    # Calls length variable
    for p in range(length):
        # Adds new characters to password
        password += secrets.choice(characters)
    # Prints generated passwords
    print(password)
