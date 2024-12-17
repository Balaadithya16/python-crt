n=list(map(int,input("Enter a quantity:").split()))
m=int(input("Enter no. of people:"))
c=0
for i in range(len(n)):
    if n[i]%m==0:
        c+=n[i]//m
    else:
        c+=(n[i]//m)+1
print(c)








