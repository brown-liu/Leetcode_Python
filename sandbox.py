def myPow(self, x: float, n: int) -> float:
    total = 1
    if x == 0:
        return 0
    for _ in range(1, n + 1):
        total *= x
    if x > 0:
        return abs(total)
    else:
        return 1.0 / abs(total)
