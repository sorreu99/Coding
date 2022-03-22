from idna import valid_contextj


class Node:
    def __init__(self,val) -> None:
        self.left=None
        self.right=None
        self.val=val


def isSametree(p,q):
    if  p is None and q is None:
        return True
    if not p or not q or p.val != q.val:
        return False
            
    return (isSametree(p.left,q.left) and isSametree(p.right,q.right))
        


root = Node(10)
root.left = Node(1)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

root1 = Node(10)
root1.left = Node(11)
root1.left.left = Node(7)
root1.right = Node(9)
root1.right.left = Node(15)
root1.right.right = Node(8)

print(isSametree(root,root1))
