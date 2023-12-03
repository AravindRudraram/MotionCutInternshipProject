import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count):
    passwords = []
    for i in range(count):
        password_length = int(input(f"Enter the length of password {i + 1}: "))
        password = generate_password(password_length)
        passwords.append(password)
    return passwords

if _name_ == "_main_":
    try:
        # Get user input for the number of passwords
        num_passwords = int(input("Enter the number of passwords to generate: "))

        # Generate and display passwords
        passwords = generate_multiple_passwords(num_passwords)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the number of passwords.")
