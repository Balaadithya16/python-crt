l=["Adithya@gmail.com","Kaif2000@gmail.com","ml2004@gmail.com","abu2005@gmail.com"]
b=True
while(b):
    a=input("Enter mail id:")
    if a in l:
        print("Alread exits")
    else:
        print("Mail created")
        b=False
        l.append(a)
print(l)