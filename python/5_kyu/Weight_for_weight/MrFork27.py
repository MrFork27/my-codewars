from collections import Counter


def order_weight(string):
    weights = sorted(string.strip().split())
    formatted_weights = {
        idx: sum(int(digit) for digit in weight) for idx, weight in enumerate(weights)
    }
    ordered_weights = {
        key: value
        for key, value in sorted(formatted_weights.items(), key=lambda item: item[1])
    }

    return " ".join(weights[key] for key in ordered_weights).strip()
