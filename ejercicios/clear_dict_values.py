# **********************
# BORRANDO VALORES CLAVE
# **********************


def run(items: dict) -> dict:
    items_values = []
    citems = {item: items_values for item in items.keys()}
    # for item in items.keys():
    #    citems[item] = items_values

    return citems


if __name__ == "__main__":
    run({"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]})
