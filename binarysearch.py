b=True
def binary(lis,n):
    lis.sort()
    #3,5,6,8,9,11
    l=0
    r=len(lis)-1
    global b
    while(b):
        mid=(l+r)//2
        if lis[mid]==n:
            b=False
            print("The position",n,"is",mid+1)
        else:
            if lis[mid]<n:
                l=mid+1
            else:
                r=mid-1
        if(l>r):
            break
li=[3,6,8,5,9,11]
a=int(input("Enter:"))
binary(li,a)
if b:
    print("not found")
