# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    def perfect_num(y: int) -> int:
        num_perfect = 0
        for i in range(1, y):
            if y % i == 0:
                num_perfect += i
        return num_perfect

    if n == perfect_num(n):
        return True
    else:
        return False
