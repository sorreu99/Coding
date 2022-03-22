from csv import list_dialects


class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None


def kthsmallest(A, B):
        lisst=[]
        def preorder(A,lisst):
            if A is not None:
                lisst.append(A.val)
                preorder(A.left,lisst)
                preorder(A.right,lisst)
        
        preorder(A,lisst)
        lisst.sort()
        print(lisst)
        return lisst[B-1]


root = Node(7)
root.left = Node(2)
root.left.left = Node(1)
# root.left.right = Node(4)
root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)

print(kthsmallest(root,2))