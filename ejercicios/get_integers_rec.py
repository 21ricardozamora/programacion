def get_int() -> int:
    number_asked = input("Give a number ")
    try:
        result = int(number_asked)
        return result
    except ValueError:
        print("Give a NUMBER!! ")
        return get_int()


if __name__ == "__main__":
    number = get_int()
