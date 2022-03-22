class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


class solution:
    def answer(self,root,B):
        def  sol(root,B,val):
            if root is None:
                return 0
            print(val)
            val+=root.val
            print(val)
            if val > B:
                return 0
            print(val)
            if root.left is None and root.right is None:
                if val==B:
                    return 1
            print(val)
            return (sol(root.left,B,val) or sol(root.right,B,val))
        

        return sol(root,B,0)


root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

soll=solution()
print(soll.answer(root,11))