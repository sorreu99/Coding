def permute(strr):
    print(type(strr))
    i = 0
    h = len(strr)
    perm = []

    def permute(strr, i, h):
        if i == h:
            perm.append("".join(strr))
        else:
            for j in range(i, h):
                print(1)
                strr[i], strr[j] = strr[j], strr[i]
                permute(strr, i+1, h)
                strr[i], strr[j] = strr[j], strr[i]
    permute(list(strr), i, h)
    return perm


x = permute('abc')
print(x)
