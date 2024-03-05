def pick_peaks(arr):
    pos = []
    peaks = []
    is_going_up = False
    repeat_index = 0

    for idx, value in enumerate(arr):
        if (idx + 1) < len(arr):
            if value > arr[idx + 1]:
                if is_going_up:
                    pos.append(repeat_index)
                    peaks.append(value)
                    is_going_up = False
                repeat_index = idx + 1
            elif value < arr[idx + 1]:
                is_going_up = True
                repeat_index = idx + 1

    return {"pos": pos, "peaks": peaks}
