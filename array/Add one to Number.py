A=[9,9,9]
val=1
for i in range(len(A)-1,0,-1):
    val=val+A[i]
    borrow=val/10
    if borrow==0:
        A[i]=val
    else:
        val = borrow


