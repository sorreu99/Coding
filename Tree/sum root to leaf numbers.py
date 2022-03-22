class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


class solution:
    def sol(self,root):
        def preorder(root,val):
            if root is None:
                return 0
            val=val*10+root.val
            if root.left is None and root.right is None:
                return val
            return( preorder(root.left,val) +
                    preorder(root.right,val))
        return  preorder(root,0)
    
        


root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

soll=solution()
print(soll.sol(root))
