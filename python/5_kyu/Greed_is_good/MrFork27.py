def score(dice):
    points = 0
    one_count = dice.count(1)
    five_count = dice.count(5)
    two_count = dice.count(2)
    three_count = dice.count(3)
    four_count = dice.count(4)
    six_count = dice.count(6)

    if one_count >= 3:
        points = 1000
        one_count = one_count - 3
    if five_count >= 3:
        points = points + 500
        five_count = five_count - 3

    if two_count >= 3:
        points = points + 200
    if three_count >= 3:
        points = points + 300
    if four_count >= 3:
        points = points + 400
    if six_count >= 3:
        points = points + 600

    points = points + one_count * 100 + five_count * 50

    return points
