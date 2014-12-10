def last_index_of(item, arr, i=0, last_index=-1):
    if i >= len(arr):
        return last_index
    elif arr[i] == item:
        return last_index_of(item, arr, i + 1, i)
    else:
        return last_index_of(item, arr, i + 1, last_index)



print str(last_index_of(5, [1, 2, 4, 6, 5, 2, 7])) + " == 4"
print str(last_index_of(5, [1, 2, 4, 6, 2, 7])) + " == -1"
print str(last_index_of(5, [1, 2, 5, 4, 6, 5, 2, 7])) + " == 5"
