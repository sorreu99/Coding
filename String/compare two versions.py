A="1.0"
B="1"
c=list(map(int,A.split(".")))
d=list(map(int,B.split(".")))
while len(c)>len(d):
    d.append(0)
while len(d)>len(c):
    c.append(0)
print(c)
print(d)
if c>d:
    print(1)
elif d>c:
    print(-1)
else:
    print(0)