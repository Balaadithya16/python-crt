l=[]
for i in range(5):
    a=int(input("Enter"))
    l.append(a)
b=[]
c=[]
for i in range(len(l)):
    if l[i] not in b:
        b.append(l[i])
    else:
        c.append(l[i])
print(c)