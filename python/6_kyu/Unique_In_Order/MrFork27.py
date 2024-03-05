def unique_in_order(sequence):
    items_list = []

    for index, item in enumerate(sequence):
        if index == 0:
            items_list.append(item)
        elif item != sequence[index - 1]:
            items_list.append(item)

    return items_list
