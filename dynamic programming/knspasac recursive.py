
wt=[1,4]
val=[3,2]
W=10
n=len(wt)
def knapsac(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+knapsac(wt,val,W-wt[n-1],n-1),knapsac(wt,val,W,n-1))
    elif wt[n-1] > W:
        return knapsac(wt,val,W,n-1)

print(knapsac(wt,val,W,n))