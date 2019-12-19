""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


# O(n) time | O(d) space
def checkBST(root: int) -> bool:
    return checkBSTHelper(root, float("-inf"), float("inf"))


def checkBSTHelper(root: int, lower: int, larger: int) -> bool:
    if root is None:
        return True
    if root.data < lower or root.data >= larger:
        return False

    return checkBSTHelper(root.left, lower, root.data) and checkBSTHelper(root.right, root.data, larger)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


node = Node(4)
node.left = Node(2)
node.left.left = Node(1)
node.right = Node(6)
node.right.left = Node(5)
node.right.right = Node(7)
print(checkBST(node))
