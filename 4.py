r=int(input("Enter:"))
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    for l in range(2,i+2):
        print(l,end="")
    print()