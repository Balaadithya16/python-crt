def push():
    a=int(input("Enter push element:"))
    l.insert(0,a)
def pop():
    if len(l)==0:
        print("Stack is empty")
    else:
        print("The pop element is",l[0])
        l.remove(l[0])
def exit():
    return False
l=[] 
z=True
print("Select the option")
print("1.push")
print("2.pop")
print("3.exit")
while(z):
    ch=int(input("enter your choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        print("Exit....")
        z=exit()
    else:
        print("Please Enter valid choice")
print("The stack elements are:",l)
