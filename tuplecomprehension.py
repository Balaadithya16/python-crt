#same like list... just convert tuple into list
#syntax: expression  loop  condition
a=(1,2,3,4)
b=list(i*i for i in a)
c=list(i*i for i in a if i*i>=4)
a=tuple(b)
print(a)
a=tuple(c)
print(a)
