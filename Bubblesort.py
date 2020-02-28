import random
def bubblesort(l):
    n=len(l)
    for i in range(n-1): 
        for j in range(n-1-i):
             if l[j+1]<l[j]: 
                l[j+1], l[j]=l[j], l[j+1]  
    return l
l=[random.randint(1,100) for i in range(6)]
print('Before sorting')
print(l)
res=bubblesort(l)
print('After sorting')
print(res)
