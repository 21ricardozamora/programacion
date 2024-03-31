# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words: list) -> list:
    lower_words = []
    upper_words = []
    for word in words:
        if word == word.upper():
            upper_words.append(word)
        elif word == word.lower():
            lower_words.append(word)
    return lower_words, upper_words
