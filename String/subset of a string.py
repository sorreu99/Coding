power=set()
i=0
current=""
def powerset(S,i,current):
    if  i==len(S):
        power.add(current)
        return
    else:
        powerset(S,i+1,current+S[i])
        powerset(S,i+1,current)
    return  power

S="abc"
x=powerset(S,i,current)
print(x)