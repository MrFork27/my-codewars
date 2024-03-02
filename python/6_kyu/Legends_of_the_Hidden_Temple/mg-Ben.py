def create_line(first_X_index, second_X_index):
    first_index = min(first_X_index, second_X_index)
    last_index = max(first_X_index, second_X_index)

    line = [" "] * (last_index + 1)

    line[first_index] = "X"
    line[last_index] = "X"
    return "".join(line) + "\n"


def mark_spot(n):
    if type(n) is not int or n % 2 == 0 or n <= 0:
        return "?"

    result = ""
    for row_i in range(0, n):
        i = row_i * 2
        i_reverse = n * 2 - 2 - i
        line = create_line(i, i_reverse)
        result = result + line

    return result
