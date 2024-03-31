# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str, index: int = 0) -> int:
    VOWELS = "aeiou"
    new_text = text.lower()
    if index >= len(new_text):
        return 0
    if new_text[index] in VOWELS:
        return 1 + count_vowels(text, index + 1)
    else:
        return count_vowels(text, index + 1)
