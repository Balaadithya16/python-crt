li=[5,3,8,6,7,2]
def selection(li):
    for i in range(len(li)-1): 
        min=i
        for j in range(i+1,len(li)):
            if int(li[min])<int(li[j]):
                min=j
        li[min],li[i]=li[i],li[min]
    return li
li=["848848494994394940000000","8948998348999390990","1992393908390890000000000000"]
print(selection(li))
 10 50 100 150 200
160