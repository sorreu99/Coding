A=[1,5,3,2,4]
def CoT(A):
    n=len(A)

    k=n-1

    count=0
    A.sort()
    while k > 0:
        i=0
        j=k-1
        while (i<j):
            if A[i]+A[j]==A[k]:
                count+=1
                i+=1
            elif A[i]+A[j]<A[k]:
                i+=1
            elif A[i]+A[j]>A[k]:
                j-=1
        k-=1
        
    return count

x=CoT(A)
print(x)


