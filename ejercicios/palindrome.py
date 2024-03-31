# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    text_reverse = ""
    palindrome_text = None
    for char in text[::-1]:
        text_reverse += char
    if text == text_reverse:
        palindrome_text = True
    else:
        palindrome_text = False
    return palindrome_text
