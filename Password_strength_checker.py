# Function to check the strength of the provided password
def check_password(password):
    # Initialize a list to store missing requirements
    missing_requirements = []
    
    # Check if the password has at least 8 characters
    if len(password) < 8:
        missing_requirements.append("more characters (minimum 8)")

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        missing_requirements.append("at least one number")

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        missing_requirements.append("at least one uppercase letter")

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        missing_requirements.append("at least one lowercase letter")

    # Check if the password contains at least one special character
    special_characters = '!@#$%^&*()_+:"<>?+-'
    if not any(char in special_characters for char in password):
        missing_requirements.append("at least one special character (e.g., !@#$%^&)")

    # If there are missing requirements, return feedback to the user
    if missing_requirements:
        return f"Your password is Weak. Consider adding: {', '.join(missing_requirements)}."
    
    # If all checks are passed, the password is good
    return 'Your password is strong.'

# Get the password input from the user
user_password = input("Enter your password to check its strength: ")
print(check_password(user_password))
