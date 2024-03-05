def dig_pow(n, p):
    sum_power = sum(int(digit) ** (p + idx) for idx, digit in enumerate(str(n)))

    return sum_power / n if sum_power % n == 0 else -1
