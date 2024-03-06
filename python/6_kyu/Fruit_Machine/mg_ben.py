def get_score(fruits):
    score_rules = {
        "Wild": 10,
        "Star": 9,
        "Bell": 8,
        "Shell": 7,
        "Seven": 6,
        "Cherry": 5,
        "Bar": 4,
        "King": 3,
        "Queen": 2,
        "Jack": 1,
    }
    for fruit, score in score_rules.items():
        count = fruits.count(fruit)
        if count == 3:
            return score * 10
        elif count == 2:
            if fruit == "Wild":
                return score
            if "Wild" in fruits:
                return score * 2
            else:
                return score
    return 0


def fruit(reels, spins):
    fruit0 = reels[0][spins[0]]
    fruit1 = reels[1][spins[1]]
    fruit2 = reels[2][spins[2]]
    return get_score([fruit0, fruit1, fruit2])
