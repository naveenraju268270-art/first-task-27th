import re

def is_palindrome_phrase(phrase):
    # Keep only letters and numbers, then lowercase
    clean_text = "".join(char.lower() for char in phrase if char.isalnum())
    return clean_text == clean_text[::-1]

print(is_palindrome_phrase("A man, a plan, a canal: Panama")) # True
