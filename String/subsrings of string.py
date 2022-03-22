S="abcd"
# n=len(S)
# col=[]
# x=""
# for lenn in range(1,n+1):
#     for j in range(0,n-lenn+1):
#         end=j+lenn-1                                      # brute force approach
#         for k in range(j,end+1):
#           x+=S[k]
#         col.append(x)
#         x=""
s="abc"
x=len(s)-1
curr=""
res=[]
def sub(s,x,curr):
    if x<0:
        
        return True
    else:
        for i in range(x,-1,-1):
            
            
            curr=s[i]+curr
            res.append(curr)
            
    curr=""
    sub(s,x-1,curr)
    return res

x=sub(s,x,curr)
print(x)