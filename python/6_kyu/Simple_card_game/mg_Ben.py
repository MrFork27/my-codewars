""" 
Return -1 if card1 > card2
Return 0 if card1 = card2
Return 1 if card1 < card2
"""


def compare_cards(card1, card2):
    priority_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    card1_priority = priority_list.index(card1)
    card2_priority = priority_list.index(card2)

    if card1_priority > card2_priority:
        return -1
    if card1_priority == card2_priority:
        return 0
    return 1


def winner(deck_steve, deck_josh):
    score_steve = 0
    score_josh = 0

    for i in range(len(deck_steve)):
        steve_card = deck_steve[i]
        josh_card = deck_josh[i]

        result_compare = compare_cards(steve_card, josh_card)
        if result_compare == -1:
            score_steve = score_steve + 1
        elif result_compare == 1:
            score_josh = score_josh + 1

    if score_steve > score_josh:
        return f"Steve wins {score_steve} to {score_josh}"
    elif score_steve < score_josh:
        return f"Josh wins {score_josh} to {score_steve}"
    return "Tie"
