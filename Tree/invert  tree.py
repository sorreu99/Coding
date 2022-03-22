class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


class solution:
    def invertTree(self, A):
        def helper(A):

            if A.left  is None and A.right is None:
                return 
            
            A.left,A.right=A.right,A.left

        if A.left is not None and A.right is None:
            helper(A.left)
        if A.right is not None and A.left is None:
            helper(A.right)
        if A.left is not None and A.right is not None:
            helper(A)
        return A
        

        
root = Node(6)
root.left = Node(3)



soll=solution()
print(soll.invertTree(root))