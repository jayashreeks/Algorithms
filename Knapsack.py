def knapsack(v,w,W,n):
    items=[]
    c=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for q in range(1,W+1):
            if w[i-1]>q:
                c[i][q]=c[i-1][q]
            else:
                c[i][q]=max(c[i-1][q],v[i-1]+c[i-1][q-w[i-1]])
    k=W
    i=n
    while i>=1:
        if c[i][k]!=c[i-1][k]:
            items.append(i)
            k-=i
        else:
            pass
        i-=1
    return items
print('Enter the number of weights and values')
n=int(input())
print('Enter the weights')
w=[x for x in input().split()]
w=list(map(int,w))
print('Enter the values')
v=[y for y in input().split()]
v=list(map(int,v))
print('Enter the maximum weight')
W=int(input())
res=knapsack(v,w,W,n)
print('The set items that can be picked are:')
for i in res:
    print(i,end=' ')

