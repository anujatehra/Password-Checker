# Password Checker - Python Project

## Description:
This is a password checker written in Python. It allows users to assess the strength of their passwords based on defined security rules and optionally check if the password has appeared in known data breaches using the Have I Been Pwned (HIBP) API.

## Features:
- Validates password strength:
  - Minimum length
  - Use of uppercase and lowercase letters
  - Inclusion of digits and special characters
- Optional check against known password breaches using the HIBP API
- Command-line interface for easy interaction
- Basic error handling and user feedback

## Requirements:
- Python 3.x
- `requests` library (required for HIBP API check)

## How to Use:
1. Clone or download this repository.

2. Open a terminal or command prompt.

3. Run the script using: python password_checker.py
   
4. Follow the prompts:

Enter the password you want to check.

Choose whether to check for known data breaches.

Note:
Internet connection is required for the optional HIBP breach check.

The HIBP check uses k-Anonymity and only partial SHA-1 hashes to protect your privacy.

Do not use this script to test passwords that you do not own or have permission to use.

License:
This project is licensed under the MIT License.

Author:
Anuja Tehra
