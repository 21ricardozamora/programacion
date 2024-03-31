# *******************
# NÚMERO EN INTERVALO
# *******************


def in_range(value: int, lower_limit: int, upper_limit: int) -> bool:
    if value > upper_limit:
        return False

    elif value >= lower_limit:
        return True
    elif value <= upper_limit:
        return True
