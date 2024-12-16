r=9
c=1
for i in range(r):
    for j in range(r-i):
        if i==0 and j==r-1:
            print("",end="")
        else:
            print("*",end="")
    for k in range(2*i-1):
        print(" ",end="")
    for l in range(r-i):
        print("*",end="")
    print()
for i in range(r-1,-1,-1):
    for j in range(r-i):
        if i==0 and j==r-1:
            print("",end="")
        else:
            print("*",end="")
    for k in range(2*i-1):
        print(" ",end="")
    for l in range(r-i):
        print("*",end="")
    print()
