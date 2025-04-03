import random
import string

# Function to generate a strong password
def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase  # a-z
    uppercase_letters = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Special characters

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Main program
def main():
    print("Welcome to the Strong Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length must be at least 8 characters. Setting length to 8.")
            length = 8

        password = generate_password(length)
        print(f"\nYour strong password is: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()