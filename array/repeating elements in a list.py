# Input : n = 7 and array = [1, 2, 3, 6, 3, 6, 1]
# Output: 1, 3, 6
# [1,1,1,2,3,3,6,6]
# Input : n = 5 and array = [1, 2, 3, 4 ,3]
# Output: 3
array = [1, 2, 3, 6, 3, 6, 1,2,9,9]
res_dict = {}
result=[]
for  x in array:
    res_dict[x]=0

for x in array:
    res_dict[x]+=1

# {1: 2, 2: 1, 3: 2, 6: 2}

for x,y in res_dict.items():
    if y > 1:
        result.append(x)

print(result)
        


  
