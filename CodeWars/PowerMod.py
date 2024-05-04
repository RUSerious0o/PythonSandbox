def power_mod(x, y, n):
    if y < 100:
        return x ** y % n
    else:
        if y % 2 == 0:
            return power_mod(x, y // 2, n) ** 2 % n
        else:
            return (power_mod(x, (y - 1) // 2, n) ** 2 % n) * x % n