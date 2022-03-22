A=[2, 3 ,1 ,1 ,2 ,4 ,2 ,0 ,1 ,1]


def minimum_jumps(A):
    l=len(A)
    i=0
    count=0
    while i<len(A):
        flag=1
        a=i
        i=i+A[i]
        if i == a:
            flag=0
        if flag==1:
            count+=1
        elif flag==0:
            return -1
        if i>=len(A)-1:
            return count

print(minimum_jumps(A))

