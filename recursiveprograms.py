#factorial
'''def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1) 
a=int(input("Enter:"))
for i in range(1,a+1):
    print(fact())'''


#fibbonocci
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
a=int(input("Enter:"))
for i in range(a):
    print(fib(i))