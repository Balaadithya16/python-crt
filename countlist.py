a=[6,3,6,7,2,7,2]
b=[]
for i in a:
    c=0
    for j in range(len(a)):
         if a[j] not in b:
            if a[j]==i:
                 c+=1
    if i not in b:
        print(i,":",c)
        b.append(i)
