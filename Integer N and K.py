n=int(input())
k=int(input())
l=[]
for i in range(n):
    d=str(input())
    t=tuple(map(int,d.split(',')))
    le=[len(str(q)) for q in t]
    if k not in le:
        l.append(t)
print(l)