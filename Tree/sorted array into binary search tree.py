class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


nums=[1,2,3,4,5]
def convArrayToBST(nums):
    
    def helper(nums,l,r):
        if l>r:
            return None
        mid=(l+r)//2

        root=Node(nums[mid])
        root.left=helper(nums,l,mid-1)
        root.right=helper(nums,mid+1,r)

    return helper(nums,0,len(nums)-1)




