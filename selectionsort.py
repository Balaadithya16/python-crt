li=[5,3,8,6,7,2]
def selection(li):
    for i in range(len(li)-1): 
        min=i
        print("The",i+1,"step:")
        for j in range(i+1,len(li)):
            if li[min]>li[j]:
                min=j
        li[min],li[i]=li[i],li[min]
        print(li)
li=[7,8,4,9,57,86]
selection(li)

