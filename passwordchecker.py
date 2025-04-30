import re

def check_password_strength(password):
    # Define patterns
    length_error = len(password) < 8
    uppercase_error = not re.search(r'[A-Z]', password)
    lowercase_error = not re.search(r'[a-z]', password)
    digit_error = not re.search(r'\d', password)
    special_char_error = not re.search(r'[\W_]', password)  # \W matches any non-word character

    # Count how many criteria are fulfilled
    passed_criteria = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Determine strength level
    if passed_criteria <= 2:
        strength = "Weak"
    elif passed_criteria == 3 or passed_criteria == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Feedback
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters.")
    if uppercase_error:
        feedback.append("Include at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Include at least one lowercase letter.")
    if digit_error:
        feedback.append("Include at least one number.")
    if special_char_error:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    return strength, feedback


# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    strength, issues = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength}")
    if issues:
        print("Suggestions to improve your password:")
        for issue in issues:
            print(f" - {issue}")
