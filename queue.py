def enque():
    a=int(input("Enter enque element:"))
    l.append(a)
def deque():
    if len(l)==0:
        print("queue is empty")
    else:
        print("The deque element is",l[0])
        l.remove(l[0])
def exit():
    return False
l=[] 
z=True
print("Select the option")
print("1.enque")
print("2.deque")
print("3.exit")
while(z):
    ch=int(input("enter your choice:"))
    if ch==1:
        enque()
    elif ch==2:
        deque()
    elif ch==3:
        print("Exit....")
        z=exit()
    else:
        print("Please Enter valid choice")
print("The queue elements are:",l)
