a=(2,3,4)
b=list(2*i for i in a)
a=tuple(b)
print(a)
c=int(input("Enter element:"))
for i in range(len(a)):
    if c==a[i]:
        print(i)
        break
