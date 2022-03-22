


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def BalancedTree(root):
    if root is None:
        return True
    countL=0
    countR=0

    def helper(p,q,countL,countR):
        if not p and q :
            countR+=1
            countL=0
        if p and  not q :
            countL+=1
            countR=0
        if p and q:
            countL=0
            countR=0
        if abs(countL-countR) >1:
            return False
        if p:
            helper(p.left,p.right,countL,countR)
        if q:
            helper(q.left,q.right,countL,countR)

        

    return helper(root.left,root.right,countL,countR)


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.right.right=Node(3)
root.right.right.right=Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
print(BalancedTree(root))