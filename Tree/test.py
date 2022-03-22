sr="google"


def isPalindrome(sr,lt,rt,hashset):
    while lt>=0 and rt<len(sr)and (sr[lt]==sr[rt]) :
        hashset.add(sr[lt:rt+1])
        lt-=1
        rt+=1

str_length=len(sr)
i=0

hashset=set()
while i < str_length:
    j=i
    isPalindrome(sr,i,j,hashset) #oddd length palindrome


    isPalindrome(sr,i,j+1,hashset) #even length palindrome
    i+=1

print(hashset)

