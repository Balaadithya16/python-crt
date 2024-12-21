def push(q):
    for i in range(len(q)//2):
        st1.insert(0,q[i])
    for i in range(len(q)//2,len(q)):
        st2.insert(0,q[i])   
def enque(st1,st2):
    for i in range(len(st2)):
        q2.insert(0,st2[i])
        q2.insert(0,st1[i]) 
q1=[1,2,3,4,5,6]
st1=[]
st2=[]
q2=[]
push(q1)
enque(st1,st2)
print(q2)