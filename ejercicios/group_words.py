# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    # TU CÓDIGO AQUÍ
    group_words = {}
    words_list = []
    for word in words:
        initials = word[0]
        if initials in group_words:
            group_words[initials].append(word)
        else:
            group_words[initials] = [word]

    return group_words


if __name__ == "__main__":
    run(
        [
            "mesa",
            "móvil",
            "barco",
            "coche",
            "avión",
            "bandeja",
            "casa",
            "monitor",
            "carretera",
            "arco",
        ]
    )
