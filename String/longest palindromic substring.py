stringg="google"
a=set()
bb=[]
def LongestPalindrome(stringg,lt,rt,a):
    while lt>=0 and rt <len(stringg) and stringg[lt]==stringg[rt]:
        if stringg[lt]==stringg[rt]:
            a.add(stringg[lt:rt+1])
            lt-=1
            rt+=1
    return a
    
l=0
r=0
def isPalindrome(stringg,l,r,a):
    for l in range(0,len(stringg)):

       LongestPalindrome(stringg,l,l,a) 
       a=LongestPalindrome(stringg,l,l+1,a)


    print(max(a,key=len))
 
        
        
    

isPalindrome(stringg,l,r,a)
