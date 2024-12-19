'''a=[10,20,30]
def sq(x):
    t=x**2
    return t
for i in a:
    print(sq(i))'''


a=[10,20,30]
def sq(x):
    t=x**2
    return t
b=list(map(sq,a))
print(b)

'''a=["2","3","4"]
b=list(map(int,a))
print(b)'''

