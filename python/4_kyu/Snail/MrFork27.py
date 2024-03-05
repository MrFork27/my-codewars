def snail(snail_map):
    # The 0x0 (empty matrix)
    if len(snail_map) == 1:
        return snail_map[0]

    n = len(snail_map)
    snail_map_n = [snail_map[i][j] for i in range(n) for j in range(n)]
    snail_index = 0
    snail = []
    op_range = [1, n, -1, -n]
    op_range_index = 0

    for k in range(n):
        snail.append(snail_map_n[snail_index])
        snail_index = snail_index + op_range[op_range_index]

    op_range_index = op_range_index + 1

    for j in reversed(range(1, n)):
        for i in range(2):
            for k in range(j):
                snail_index = snail_index + op_range[op_range_index]
                snail.append(snail_map_n[snail_index - 1])
            op_range_index = (op_range_index + 1) % len(op_range)

    return snail
