"""
In this code:

We import the random module to generate random characters and the string module to access character sets like letters, digits, and punctuation.
The generate_password function takes an optional length parameter to specify the length of the password (default is 12 characters).
It defines a character set that includes uppercase letters, lowercase letters, digits, and punctuation.
It generates a random password by randomly selecting characters from the defined character set and concatenating them to create the password.
You can adjust the password_length variable to generate passwords of different lengths.
"""

import random
import string

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 12  # You can change this to your desired password length
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
