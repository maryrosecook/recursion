"""n musical Hacker Schoolers are playing one of 7 notes, each on a
different instrument. What are all the possible tones? (example: ["A",
"A", "B"] would be one if there n were 3)"""

from flatten import flatten
from test import test

NOTES = ["A", "B", "C"]

def tones(player_count, tone=[]):
    if not player_count:
        return " ".join(tone)
    else:
        ts = []
        for n in NOTES:
            t = tone[:]
            t.append(n)
            ts.append(tones(player_count - 1, t))

        return ts

test(flatten(tones(0)), [])
test(flatten(tones(2)), ['A A', 'A B', 'A C', 'B A', 'B B', 'B C', 'C A', 'C B', 'C C'])
