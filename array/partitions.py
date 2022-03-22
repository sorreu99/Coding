B = [1, 2, 3, 0, 3]
summ=0
count=0
i=0
y=sum(B)//3
while i < len(B):
    summ+=B[i]
    if summ== y:
        count+=1

        summ=0

    i+=1
print(count)


    



