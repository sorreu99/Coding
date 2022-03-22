A = [1, 2, 3, 4, 6]

# def FinMis(A):
#     l=len(A)
#     A.sort()
#     for i in range(len(A)):
#         if A[i]-1!=i:
#             return i+1


# p=FinMis(A)
# print(p)

def FinMis(A):
    miss = 0
    for i in A:
        miss = miss ^ i
    for i in range(1, len(A)+2):
        miss = miss ^ i
    return miss


x = FinMis(A)
print(x)
