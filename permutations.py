from test import test
import itertools

def flatten(l):
    f = []
    for item in l:
        if type(item) == list:
            f.extend(flatten(item))
        else:
            f.append(item)
    return f

def permutations(s, prefix=""):
    if not s:
        return [prefix]
    else:
        return [permutations(s[:i] + s[i+1:], prefix + c)
                for i, c in enumerate(s)]

## test helpers

def lists_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        for l1_item in l1:
            if not l1_item in l2:
                return False

    return True

def str_chars(cs):
    return ["".join(p) for p in list(cs)]

## tests

s = "abcd"
test(sorted(flatten(permutations(s))),
     sorted(str_chars(itertools.permutations(s, len(s)))))

s = ""
test(sorted(flatten(permutations(s))),
     sorted(str_chars(itertools.permutations(s, len(s)))))
