from idna import valid_contextj


class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


preorder(root)