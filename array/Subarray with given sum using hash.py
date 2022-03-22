A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 15


def SubSum(A, s):
    i = 0
    col = {}
    current_summ = 0
    while i < len(A):

        current_summ = current_summ+A[i]

        if current_summ not in col:
            col[current_summ] = i
        if current_summ-s == 0:
            return [0, i]
        print(col[current_summ])
        print('cursum', current_summ)
        if current_summ - s in col and (col[current_summ-s]+1 <= i):
            return [col[current_summ-s]+1, i]
        i += 1

    return -1


y = SubSum(A, s)
print(y)
