a=121
ans=0
while a>0:
    temp=a%10
    ans=ans*10+temp
    a/=10
print(ans)
