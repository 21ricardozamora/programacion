# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    item_values = list(items.values())
    all_same = True
    for item in item_values:
        if item != item_values[1]:
            all_same = False
        break
    return all_same


if __name__ == "__main__":
    run({"a": 1, "b": 1, "c": 1, "d": 1})
