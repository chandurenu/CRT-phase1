#a shopping mall having 5% discount for men and 7% discount for women and individual discount for each time they purchase is 3 into number of items is purchased
d={}
n=int(input("Enter no of items: "))
for i in range(n):
    k=input("Enter item: ")
    v=int(input("Enter item price: "))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("Enter Gender: ")
if g == "male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*5/100
j=0
print("items - prices : discount-prices")
for i in d:
    print(f"{i} - {d[i]} : {l[j]}")
    j+=1
else:
    print("*"*20)
print(f"Total bill : {bill}")
