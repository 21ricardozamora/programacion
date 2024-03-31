# ********
# PANGRAMA
# ********


def is_pangram(text: str) -> bool:
    ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
    ALPHABET_SIZE = len(ALPHABET)
    counter = 0
    pangram = set()
    for char in text.lower():
        if char in ALPHABET:
            if char not in pangram:
                counter += 1
                pangram.add(char)
    if counter == ALPHABET_SIZE:
        return True
    else:
        return False


is_pangram("The quick brown fox jumps over the lazy dog")
