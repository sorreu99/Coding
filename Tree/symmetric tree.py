class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def isSymmetric(root):
    if root is None or root.left is None and root.right is None :
        return True
    p=root.left
    q=root.right

    def helper( p , q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (helper(p.left,q.right) and helper(p.right,q.left))
    return helper(p,q)



def isSymmetric2(root):
    if root is None:
        return True
    p=[]
    q=[]
    p.append(root.left)
    q.append(root.right)
    while p and q:
        n1=p.pop(0)
        n2=q.pop(0)
        if n1 and n2:
            print(n1.val,n2.val)
        if not n1 and not n2:
            return True
        if not n1 or not n2 or n1.val != n2.val:
            
            return False
        p.append(n1.left)
        p.append(n1.right)
        q.append(n2.right)
        q.append(n2.left)
    return True



root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left=Node(4)
root.right.right=Node(3)


print(isSymmetric(root))
print(isSymmetric2(root))


    
