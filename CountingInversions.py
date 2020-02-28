import random
def mergecount(m,n):
    mergelist= []
    (i,j) = (0,0)
    count = 0
    while i < len(m) and j < len(n):
        if m[i] < n[j]:
            mergelist.append(m[i])
            i += 1
        elif n[j] < m[i]:
            mergelist.append(n[j])
            j += 1
            count += (len(m)-i)
    mergelist += m[i:]
    mergelist += n[j:]
    return (mergelist,count)


def sortcount(l):
    if len(l) < 2:
        return l, 0
    mid = len(l) // 2
    (A,ra) = sortcount(l[:mid])
    (B,rb) = sortcount(l[mid:])
    (result, count)= mergecount(A,B)
    count += (ra + rb)
    return (result, count)
l1=[random.randint(1,50) for x in range(10)]
(l1,answer)=sortcount(l1)
print('Number of inversions:',answer)
