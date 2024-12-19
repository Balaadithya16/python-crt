'''add=lambda x,y:x+y
z=add(2,4)
print(z)'''

'''n=[3,8,5,4,6,5]
a=list(filter(lambda n: n%2==0,n))
print(a)'''

'''n=[3,8,5,4,6,7]
b=lambda n:n%2==0
a=list(filter(b,n))
print(a)'''

n=[3,8,5,4,6,7]
b=lambda n:n%2==0
c=lambda n:n%2!=0
a=list(filter(b,n))
d=list(filter(c,n))
print(a)
print(d)


'''def odd(x):
    return x%2!=0
n=[3,8,5,4,6,5]
b=list(filter(odd,n))
print(b)'''


'''def even(x):
    return x%2==0
def odd(x):
    return x%2!=0
n=[3,8,5,4,6,5]
b=list(filter(even,n))
print(b)
c=list(filter(odd,b))
print(c)'''
