n=int(input())
for i in range(2,(n**o.5)+1):
    if n%i==0:
        print("Not a Prime")
        break
else:
    print("Prime")
