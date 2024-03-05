def narcissistic(value):
    digits = [int(digit) for digit in str(value)]
    digits_sum = sum([number ** len(str(value)) for number in digits])

    return True if digits_sum == value else False
