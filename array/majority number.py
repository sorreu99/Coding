a=[22,2,2,2,4,4]

count=0
candidate=None

for  i in a:
    if count==0:
        candidate=i
    count = count + 1 if  i==candidate else count-1
print(candidate)