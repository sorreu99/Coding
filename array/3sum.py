nums = [-1,0,1,2,-1,-4]

def solution(nums):
    result=[]
    nums.sort()

    for i in range(0,len(nums)):
        j=i+1
        k=len(nums)-1
        if i > 0 and nums[i]==nums[i-1]:
            continue
        while j<k:
            summ=nums[j]+nums[k]+nums[i]
            if summ==0:
                result.append([nums[i],nums[j],nums[k]])
                k-=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
            if summ<0:
                j+=1
            elif  summ>0:
                k-=1
    return result

print(solution(nums))

 
        
