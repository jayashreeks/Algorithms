import random
def bsearch(l,ele,beg,end):
    if beg<=end:
        mid=(beg+end)//2
        if l[mid]==ele:
            return mid
        elif l[mid]<ele:
            return bsearch(l,ele,mid+1,end)
        else:
            return bsearch(l,ele,beg,mid-1)
    else:
        return -1
    
l=[random.randint(1,100) for i in range(6)]
print('The array is:')
print(l)
ele=int(input('Enter the element to be searched\n'))
beg=0
end=len(l)-1
l=sorted(l)
print('sorted list ',l)
res=bsearch(l,ele,beg,end)
if res!=-1:
    print(ele,'Found at position',res+1)
else:
    print(ele,'Not Found')
