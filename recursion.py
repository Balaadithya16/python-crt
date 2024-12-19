import sys
print(sys.getrecursionlimit())
c=1
def great():
    global c
    print("Hai guys",c)
    c+=1
    if c<=500:
        great()
great()

#we use set for recursion limit
'''import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(501))
c=1
def great():
    global c
    print("Hai guys",c)
    c+=1
    great()
great()'''

