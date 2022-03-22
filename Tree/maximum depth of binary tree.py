from unittest.util import _MAX_LENGTH


class Node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val

def maxLength(root):
    if root is None:
            return 0
    return (1+ max(maxLength(root.left),maxLength(root.right))) 


root=Node(2)
root.left=Node(2)
root.left.left=Node(3)
root.right=Node(6)
root.right.right=Node(6)
root.right.right.right=Node(6)

print(maxLength(root))