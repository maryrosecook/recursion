"""How many different ways can we make change of $\$ 1.00$, given
half-dollars, quarters, dimes, nickels, and pennies?"""

from test import test

COINS = [50, 25, 10, 5, 1]

def change(coins, amount):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    else:
        return sum([change(coins[i:], amount - c) for i, c in enumerate(coins)])



test(change(COINS, 100), 292)
