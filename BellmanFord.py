from collections import defaultdict 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = []
        
    def addEdge(self,u,v,w): 
        self.graph.append([u, v, w])

    def printPath(self,parent, j):  
        if parent[j] == -1 :
            for k in d.keys():
                if d[k]==j:
                    x=k
            print(x,end='')
            return
        self.printPath(parent , parent[j])
        for k in d.keys():
                if d[k]==j:
                    x=k
        print(x,end='')
          
    def printArr(self, dist, parent): 
        print("Vertex   Distance from Source\tPath") 
        for i in range(self.V):
            for k in d.keys():
                if d[k]==i:
                    x=k
            print("%c \t\t %d\t\t" % (x, dist[i]),end='')
            self.printPath(parent,i)
            print()
      
    def BellmanFord(self, src): 

        dist = [float("Inf")] * self.V 
        dist[src] = 0 
        parent=[-1]*self.V
        
        for i in range(self.V - 1): 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w
                        parent[v]=u
  
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print("Graph contains negative weight cycle")
                        return
        self.printArr(dist,parent)
        
n=int(input('Enter the number of vertices\n'))
print('Enter the vertices')
d={}
for i in range(n):
    c=input()
    d[c]=i
v=int(input('Enter the number of edges\n'))
g = Graph(n) 
for i in range(v):
    u,v,cost=input('Enter edge(u,v) and cost:\n').split()
    u=d[u]
    v=d[v]
    cost=int(cost)
    g.addEdge(u,v,cost)
src=input('Enter the source vertex\n')
src=d[src]
g.BellmanFord(src);
