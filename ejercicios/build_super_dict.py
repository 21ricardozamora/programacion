# ***************************
# DICCIONARIO EN CONSTRUCCIÓN
# ***************************


def run(items: list) -> dict:
    first_part = None
    unpack_items = {}
    for item in items:
        if isinstance(item, list):
            first_part = item[0]
        if first_part in unpack_items:
            unpack_items[first_part].append(item)
        else:
            unpack_items[first_part] = item[1:]

    return unpack_items


if __name__ == "__main__":
    run(
        [
            ["Episode IV - A New Hope", "May 25", 1977, "George Lucas"],
            ["Episode V - The Empire Strikes Back", "May 21", 1980],
            ["Episode VI - Return of the Jedi", "May 25", 1983],
        ]
    )
