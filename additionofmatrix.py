r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[-1]
print(sum)

