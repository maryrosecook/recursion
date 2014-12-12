"""Given a deck of cards, produce every possible hand (order of cards
in hand doesn't matter)"""

from flatten import flatten
from test import test

def deck():
    return ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S",
            "10S", "JS", "QS", "KS", "AH", "2H", "3H", "4H", "5H",
            "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD",
            "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D",
            "JD", "QD", "KD", "AC", "2C", "3C", "4C", "5C", "6C",
            "7C", "8C", "9C", "10C", "JC", "QC", "KC"]


def hands(cards, hand_size, hand=[]):
    if not hand_size:
        return " ".join(hand)
    else:
        hs = []
        for i in range(0, len(cards) - hand_size + 1):
            h = hand[:]
            h.append(cards[i])
            hs.append(hands(cards[i + 1:], hand_size - 1, h))
        return hs

test(flatten(hands(["AS", "2S", "3S", "4S"], 4)), ['AS 2S 3S 4S'])
test(flatten(hands(["AS", "2S", "3S", "4S"], 3)),
     ['AS 2S 3S', 'AS 2S 4S', 'AS 3S 4S', '2S 3S 4S'])

test(len(flatten(hands(deck(), 5))), 2598960)
