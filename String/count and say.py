# A= 1,11,21,1211,111221
n=2
count=1
d={0:"1"}
j=1
while n:


    for x in d.values():
        y=""
        i=len(x)-1
        print('x',x)
        print('i',i)
        k=i
        while i !=0:
            if i-1!=0 and x[i]==x[i-1]:
                count+=1
                i-=1
                
            y=str(count)+x[k-1]+y
            k-=1
            i-=1
    n-=1
    
    d[j]=y
    j+=1
print(d)

