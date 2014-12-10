def max(numbers, largest_so_far=None):
    if not numbers:
        return largest_so_far
    elif not largest_so_far or numbers[0] > largest_so_far:
        return max(numbers[1:], numbers[0])
    else:
        return max(numbers[1:], largest_so_far)

print str(max([])) + " should be None"
print str(max([1])) + " should be 1"
print str(max([2, 1])) + " should be 2"
print str(max([1, 2, 3])) + " should be 3"
print str(max([-1, -2, -3])) + " should be -1"
