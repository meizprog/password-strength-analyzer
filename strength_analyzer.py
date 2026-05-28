import re

def check_password_strength(password):
    issues = []

    if len(password) < 8:
        issues.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        issues.append("an uppercase letter")
    if not re.search(r"[a-z]", password):
        issues.append("a lowercase letter")
    if not re.search(r"\d", password):
        issues.append("a number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("a special character")

    score = 5 - len(issues)

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, issues


password = input("Enter your password: ")
strength, issues = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if issues:
    print("\nYour password needs:")
    for issue in issues:
        print(f"  - {issue}")