
"""Prodigy_cs_03
#program to check for password complexity written by BLESSING IFEOLUWA OMOGBEHIN

import re #allows functionality provided by the Regular Expression library

def check_password_strength(password):
    #password length declaration
    if len(password) < 9:
        return "Weak: Password should be at least 9 characters long."

    # password condition declaration
    contain_uppercase = any(char.isupper() for char in password)
    contain_lowercase = any(char.islower() for char in password)
    contain_number = any(char.isdigit() for char in password)
    contain_special = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>§~]', password))

    # checking password strength based on different criteria
    if contain_uppercase and contain_lowercase and contain_number and contain_special:
        return "Strong Password: Password complexity successful."
    elif contain_uppercase and contain_lowercase and contain_number:
        return "Moderate Password: Requires special characters."
    elif contain_uppercase and contain_lowercase and contain_special:
        return "Moderate Password: Requires number."
    elif contain_uppercase and contain_lowercase:
        return "Moderate Password: Password requires number and special characters."
    elif contain_lowercase and contain_number:
        return "Weak Password: Please add uppercase and special characters."
    else:
        return "Weak Password: please check if your password meets the following criteria: uppercase, lowercase, number, and special characters."

password = input("please input your password: ")
strength = check_password_strength(password)
print(strength)