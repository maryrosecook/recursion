def sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])

print str(sum([1, 2, 3, 4, 5])) + " == 15"
print str(sum([])) + " == 0"
