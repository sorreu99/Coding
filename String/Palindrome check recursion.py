s="abaa"
i=0
j=len(s)-1
def checK(s,i,j):

    if i>j:
        return ("it is a plaindrome")
    elif s[i]!=s[j]:
        return ("not a palindrome")
    return (checK(s,i+1,j-1))

print(checK(s,i,j))


