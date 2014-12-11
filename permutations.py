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

def permutations(s, depth):
    def p(s, depth, prefix):
        if not s or not depth:
            return [prefix]
        else:
            return [p(s[:i] + s[i+1:], depth - 1, prefix + c)
                    for i, c in enumerate(s)]

    return flatten(p(s, depth, ""))

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
test(sorted(flatten(permutations(s, 2))),
     sorted(str_chars(itertools.permutations(s, 2))))

s = "abcd"
test(sorted(flatten(permutations(s, 4))),
     sorted(str_chars(itertools.permutations(s, 4))))

s = "abcd"
test(sorted(flatten(permutations(s, 1))),
     sorted(str_chars(itertools.permutations(s, 1))))

s = "abcd"
test(sorted(flatten(permutations(s, 0))),
     sorted(str_chars(itertools.permutations(s, 0))))

s = ""
test(sorted(flatten(permutations(s, 0))),
     sorted(str_chars(itertools.permutations(s, 0))))
