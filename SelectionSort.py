import random
import time
def selectionsort(l):
    n=len(l)
    for i in range(n-1): 
        min = i 
        for j in range(i+1,n):
             if l[min] > l[j]: 
                min = j 
        l[min], l[i]=l[i], l[min]  
    return l
l=[random.randint(1,100) for i in range(6)]
print('Before sorting')
print(l)
start=time.time()
res=selectionsort(l)
end=time.time()
print('Execution time=',end-start)
print('After sorting')
print(res)
