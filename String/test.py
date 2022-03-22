A="A man, a plan, a canal: Panama"
s="".join(ch.lower() for ch in A if ch.isalnum())
print(s)
print(len(s))
i=0
j=len(s)-1
def isPalindrome(s,i,j):
    if i>j:
        return 0
    elif s[i]!=s[j]:
        return 1

    return isPalindrome(s,i+1,j-1)
k=isPalindrome(s,i,j)
print(k)