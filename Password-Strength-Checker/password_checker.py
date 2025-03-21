import re

print("Enter a password to check its strength")
password = input()
print("Checking password strength...")

# Check length
if len(password) < 8:
    print("Password is weak")
else:
    # Check for special characters, numbers, and uppercase/lowercase letters
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[@$!%*?&#]', password)

    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong")
    elif has_upper and has_lower and (has_digit or has_special):
        print("Password is medium")
    else:
        print("Password is weak")
