def bubble(li):
    c=0
    for i in range(len(li)-1):
        print("The",i+1,"iteration :")
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                c+=1
                print(li,c)
    return li
l=[5,3,8,6,7,2]
bubble(l)