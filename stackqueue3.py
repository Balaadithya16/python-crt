def pop(st1):
    for i in range(len(st1)):
        enque(st1[i])
def enque(e):
    if len(q)==0:
        q.insert(0,e)
    else:
        if e<q[0]:
            q.insert(0,e)
        elif e>q[len(q)-1]:
            q.append((e))
        else:
            for i in range(len(q)-1):
                if e>q[i] and e<q[i+1]:
                    q.insert(i+1,e)
                    break
def push(q):
    for i in range(len(q)):
        ans.append(q[i])

st1=[34,3,31,98,92,23]
print(st1)
q=[]
ans=[]
pop(st1)
push(q)
print(ans)