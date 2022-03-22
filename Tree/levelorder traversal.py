class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None


def printLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        printCurrentLevel(root,i)

def printCurrentLevel(root,level):
    if level is None:
        return
    if level==1:
        print(root.val)
    if level>1:
        printCurrentLevel(root.left,level-1)
        printCurrentLevel(root.right,level-1)



def height(root):
    if root is None:
        return 0
    else:
        llength=height(root.left)
        rlength=height(root.right)
    
    if llength>rlength:
        return llength+1
    else:
        return rlength+1


root = Node(0)
root.left = Node(1)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(6)


print(printLevelOrder(root))