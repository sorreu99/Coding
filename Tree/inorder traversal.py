class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):

    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


inorder(root)
