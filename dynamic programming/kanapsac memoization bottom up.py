wt=[1,4]
val=[3,2]
W=10
n=len(wt)

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsac(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    if wt[n-1]<W:
        t[n][W]=max(val[n-1]+knapsac(wt,val,W-wt[n-1],n-1),knapsac(wt,val,W,n-1))
        return t[n][W]
    elif wt[n-1]>W:
        t[n][W]=knapsac(wt,val,W,n-1)
        return t[n][W]

print(knapsac(wt,val,W,n))
    