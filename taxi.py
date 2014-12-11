"""How many ways are there for a taxi driver to get from the top left
of a grid city to the bottom right? The city is exactly 10 blocks in
each direction, all streets are two ways, and you know the city well
enough that you'd balk if the driver actually went drove away from the
goal - so never up or left, only right and down."""

def routes(x, y, w, h):
    if x == w and y == h:
        return 1
    else:
        sum_ = 0
        if x != w:
            sum_ += routes(x + 1, y, w, h)

        if y != h:
            sum_ += routes(x, y + 1, w, h)

        return sum_

print routes(0, 0, 10, 10)
