def isort(o):
    l=o[:]
    for pos in range(1,len(l)):
        nextpos=pos
        while nextpos>0 and l[nextpos]<l[nextpos-1]:
            (l[nextpos],l[nextpos-1])=(l[nextpos-1],l[nextpos])
            nextpos-=1
    return l

l=[1,9,2,7,4,5]
p=isort(l)
print(p)
