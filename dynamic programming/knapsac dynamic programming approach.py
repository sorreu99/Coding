wt=[1,4]
val=[3,2]
W=10
n=len(wt)

t = [[0  for i in range(W + 1)] for j in range(n + 1)]

def knapsac(wt,val,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j]==0
            elif wt[i-1]<=W:
                for i in range(1,n+1):
                    for j in range(1,W+1):
                        t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[i][j]
print(knapsac(wt,val,W,n))

print(t)