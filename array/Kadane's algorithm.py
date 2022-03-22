A=[-2,-3,-4,5]

maxsofar=-100000
i=0
curr_sum=0

for i in range(len(A)):
    curr_sum=curr_sum+A[i]
    if curr_sum > maxsofar:
        maxsofar=curr_sum
    if curr_sum < 0:
        curr_sum=0
print(maxsofar)