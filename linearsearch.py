b=True
def linearsearch(l,x):
    for i in range(len(l)):
        if l[i]==x:
            global b
            b=False
            print("The",x,"position is:",i+1)
            break
li=[3,6,8,5,9,11,11]
n=int(input("Enter a number:"))
linearsearch(li,n)
if b:
    print("Not found")



