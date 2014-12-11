"""A child is running up a staircase with n steps, and can hop either
1 step, 2 steps, or 3 steps at a time. Write a function that, given
the length of the staircase, tells you how many ways there are to go
up the steps."""

from test import test

def steps(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        sum = 0
        for step in range(1, 4):
            sum += steps(n - step)

        return sum


test(steps(0), 0)
test(steps(1), 1)
test(steps(2), 2)
test(steps(3), 4)
test(steps(4), 7)
test(steps(5), 13)
