A=[-10,-10,-10]
B=-5


A.sort()
min_diff=abs(A[0]+A[1]+A[2]-B)
for i in range(len(A)):
    j=i+1
    k=len(A)-1
    while j < k:
        summ=A[i]+A[j]+A[k]
        res=abs(summ-B)
        if res <= min_diff:
                min_diff=res
                best=summ
                print(A[i],A[j],A[k])
        if summ<B:
            j+=1
        elif summ> B:
            k-=1
        if summ==B:
            print(summ)
            break
    if summ==B:
        break

print(best)


            
