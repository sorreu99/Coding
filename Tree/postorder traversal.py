from turtle import pos


class Node:
    def __init__(self,val) -> None:
        self.left=None
        self.right=None
        self.val=val


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=' ')

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

postorder(root)