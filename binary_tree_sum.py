"""Write a recursive function to compute the sum of a binary tree of numbers"""

class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

    def sum(self):
        return self.value + \
            (self.left and self.left.sum() or 0) + \
            (self.right and self.right.sum() or 0)

print str(Node(1,
               Node(2,
                    Node(3),
                    Node(4)),
               Node(5,
                    Node(6),
                    Node(7))).sum()) + " == 28"

print str(Node(1,
               Node(2,
                    Node(3)),
               Node(4)).sum()) + " == 10"
