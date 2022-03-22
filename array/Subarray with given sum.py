A=[2,1,5,8,7,9]
s=8

def SubSum(A,s):
    start=0
    j=1
    summ=A[start]
    while j <= len(A):
        
        while summ > s and start<j-1:
            summ=summ-A[start]
            start+=1
        if summ==s:
            return [start,j-1]

        if j<len(A):
            summ+=A[j]
        j+=1
            

        
    return -1

x=SubSum(A,s)
print(x)



