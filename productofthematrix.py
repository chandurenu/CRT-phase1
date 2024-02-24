r,c=int(input("Rows: ")),int(input("Colums: "))
l=[0]*r
for i in range(r):
    l[i]=(list(map(int,input().split())))
#print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)    
