# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}

    for move in imoves.split(","):
        inventory_key, inventory_moves = move[0], move[1:]

        # Manejar números negativos
        moves = (
            int(inventory_moves)
            if inventory_moves[0] != "-"
            else int(inventory_moves) * -1
        )

        # Actualizar el valor en el diccionario
        if inventory_key in inventory:
            inventory[inventory_key] += moves
        else:
            inventory[inventory_key] = moves

    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
