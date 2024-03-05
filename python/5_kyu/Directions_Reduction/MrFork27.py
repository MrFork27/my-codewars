def dir_reduc(arr):
    path_return = []
    index = 0

    while index < len(arr):
        current_dir = arr[index]

        if (index + 1) < len(arr):
            next_dir = arr[index + 1]
            north_condition = current_dir == "NORTH" and next_dir != "SOUTH"
            south_condition = current_dir == "SOUTH" and next_dir != "NORTH"
            west_condition = current_dir == "WEST" and next_dir != "EAST"
            east_condition = current_dir == "EAST" and next_dir != "WEST"

            if north_condition or south_condition or west_condition or east_condition:
                path_return.append(current_dir)
                index = index + 1
            else:
                index = index + 2
        else:
            path_return.append(current_dir)
            index = index + 1

    if len(arr) != len(path_return):
        path_return = dir_reduc(path_return)

    return path_return
