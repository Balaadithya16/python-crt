def dequeue(queue):
    for i in range(len(queue)):
        e=queue[i]
        push(e)
    queue.clear()
def push(p):
    stack.insert(0,p)
def pop(stack):
    for i in range(len(stack)):
        e=stack[i]
        enque(e)
    stack.clear()
def enque(p):
    q.append(p)
q=[1,2,3,4,5]
stack=[]
dequeue(q)
pop(stack)
print(q)





