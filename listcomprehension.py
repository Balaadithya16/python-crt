'''a=[1,2,3,4,5]
b=[]
for i in a:
    i=i*i
    b.append(i)
print(b)'''

'''a=[1,2,3,4,5]
b=[]
for i in a:
    i=i*2
    if i>4:
        b.append(i)
print(b)'''

a=[1,2,3,4,5]
#syntax:  expression loop condition.
b=[i*i for i in a]
c=[i*2 for i in a if i>4]
print(b)
print(c)