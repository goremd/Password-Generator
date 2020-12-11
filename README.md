# Password-Generator
Random selection secure password generator.

●	General Information

  o	Project Idea
  
Attempt to create a password generator that produces secure passwords with varying order of characters. Ensure user is able to request multiple passwords at once with an input request for how many characters.

  o	Identify the existing problem
  
Passwords need to be randomized in order to be as secure as possible.

●	Functional Requirements

  o	Functionality
  
  This section contains the requirements for creating Python password generator.
  
    ▪	Must require user input
    
      o	Number of passwords
      
      o	Number of characters per password
      
    ▪	Must produce randomized characters for security

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
