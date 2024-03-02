def open_or_senior(data):
    return [
        "Senior" if member[0] >= 55 and member[1] > 7 else "Open" for member in data
    ]
