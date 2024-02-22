# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    delivery = stock.get(merch, 0)
    products = stock.keys()
    available = True
    for product in stock:
        if product == merch:
            if amount > delivery:
                available = False
        elif merch not in products:
            available = False

    return available


if __name__ == "__main__":
    run({"pen": 20, "cup": 11, "keyring": 40}, "cup", 9)
