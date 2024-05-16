def get_int() -> int:
    while True:
        number_asked = input("Give me a number ")
        try:
            result = int(number_asked)
            return result
        except ValueError:
            print("Give me a NUMBER!!")


if __name__ == "__main__":
    number = get_int()
