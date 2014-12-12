def flatten(l):
    f = []
    for item in l:
        if type(item) == list:
            f.extend(flatten(item))
        else:
            f.append(item)
    return f
