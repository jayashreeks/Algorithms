def minDist(dist,queue):
    mini=float("Inf")
    min_index=-1
    for i in range(len(dist)):
        if dist[i]<mini and i in queue:
            mini=dist[i]
            min_index=i
    return min_index

def printPath(parent,j):
    if parent[j]==-1:
        print(j+1,end='')
        return
    printPath(parent,parent[j])
    print(j+1,end='')

def printSol(dist,parent):
    src=0
    print('Vertex\tDistance from source\tPath')
    for i in range(1,len(dist)):
        print(src+1,'->',i+1,' \t  ',dist[i],end='  \t\t  ')
        printPath(parent,i)
        print()

def dijkstra(graph,src):
    row=len(graph[0])
    col=len(graph[0])
    dist=[float('Inf')]*row
    dist[src]=0
    parent=[-1]*row
    queue=[]
    for i in range(row):
        queue.append(i)
    while queue:
        u=minDist(dist,queue)
        for k in range(len(queue)):
            if queue[k]==u:
                del queue[k]
                break
        for v in range(col):
            if graph[u][v] and v in queue:
                if dist[v]>dist[u]+graph[u][v]:
                    dist[v]=dist[u]+graph[u][v]
                    parent[v]=u
    printSol(dist,parent)
nov=int(input('Enter the number of vertices\n'))
noe=int(input('Enter the number of edges\n'))
g=[[0 for i in range(nov)]for j in range(noe)]
for i in range(noe):
    u,v,w=input('Enter the edge(u,v) and its cost\n').split()
    u=int(u)-1
    v=int(v)-1
    w=int(w)
    g[u][v]=w
    g[v][u]=w
src=int(input('Enter the source vertex\n'))-1
dijkstra(g,src)
