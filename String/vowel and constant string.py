


A="inttnikjmjbemrberk"


# tup=('a','e','i','u','o')
# vow=0
# cons=0
# count=0
# for i in range(len(A)):
#     if A[i] in tup:
#         vow+=1
#         count+=cons
#     else:
#         cons+=1
#         count+=vow
# print(count)
    
def solve(A):
        vowel = ['a','e','i','o','u']
        suff_count = list(A)
        v_c = 0
        for i in range(len(A)-1,-1,-1):
            if A[i] in vowel:
                v_c += 1
            suff_count[i] = v_c
        c = 0
        print(suff_count)
        for i in range(len(A)):
            if A[i] in vowel:
                c += len(A) - i - suff_count[i]
            else:
                c += suff_count[i]
        return c % 1000000007
print(solve(A))
