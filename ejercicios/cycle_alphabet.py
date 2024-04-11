# *****************
# ALFABETO CIRCULAR
# *****************


def run(max_letters: int) -> str:
    def get_alphabet_letters(max_letters: int) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        size_alphabet = len(ALPHABET)
        index = 0
        while max_letters > 0:
            yield ALPHABET[index]
            index = (index + 1) % size_alphabet
            max_letters -= 1

    text = ""
    alphabet_generator = get_alphabet_letters(max_letters)
    for char in alphabet_generator:
        text += char
    return text


if __name__ == "__main__":
    run(0)
