# def summm(n):
#     sum__r=0
#     while n >0:
#         sum__r+=n%10
#         n=n//10
#     print(sum__r)
#     return sum__r
 
# def sort(arr,n):
 
#     reslist=[]
#     for i in range(n):
#         reslist.append([summm(arr[i]),arr[i]])
#     print(reslist)
#     reslist.sort()
#     for i in range(len(reslist)):
#         print(reslist[i][1],end=" ")
 
# sort(arr,n)


# Que 3.
# What will be the output of the following code chunk.
def str_matcher(string):
    print('Inside a string matcher')
    print('String is '+ string)  
def list_matcher(lis):
    print('Inside a list matcher')
    print('list is '+ lis)
    
def get_matcher(type_):
    switcher = {'str': str_matcher, 'list': list_matcher}
    return switcher[type_]

matcher = get_matcher('str')
matcher('Mayank')
# Ans: string is mayank