# Password Strength Checker

## Overview
This is a simple Python script that evaluates the strength of a user-provided password. It checks for password length, the presence of uppercase and lowercase letters, digits, and special characters.

## Features
- Checks if the password is at least **8 characters long**.
- Evaluates the presence of:
  - **Uppercase letters (A-Z)**
  - **Lowercase letters (a-z)**
  - **Digits (0-9)**
  - **Special characters (@$!%*?&#)**
- Classifies password strength as **Weak**, **Medium**, or **Strong**.

## Usage
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/password-checker.git
cd password-checker
```

### 2. Run the Script
```sh
python password_checker.py
```

### 3. Enter a Password
The script will prompt you to enter a password and return an evaluation of its strength.

## Example Output
```sh
Enter a password to check its strength
> P@ssw0rd
Checking password strength...
Password is strong
```

## Requirements
- Python 3.x

