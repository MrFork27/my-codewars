def count_bits(n):
    one_bits = 0

    # Check that input is non-negative
    if n < 0:
        raise ValueError("Input is negative")

    # Represent n binary
    binary_number = "{0:b}".format(n)

    # Count the number of bits that are equal to one
    for i in range(0, len(binary_number)):
        if binary_number[i] == "1":
            one_bits = one_bits + 1

    return one_bits
