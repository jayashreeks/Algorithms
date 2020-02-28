from collections import defaultdict 
class Graph: 
    def __init__(self,vertices):
        self.V=vertices
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def DFSUtil(self,visited,u):
        print(u,end=' ')
        for i in self.graph[u]:
            if visited[i]==False:
                visited[i]=True
                self.DFSUtil(visited,i)
    def DFS(self,u):
        visited=[False]*self.V
        visited[u]=True
        self.DFSUtil(visited,u)
 
q=int(input('enter no. of edges\n'))
nov=int(input('enter no. of vertices\n'))
g = Graph(nov)
for i in range(q):
    a,b=input("enter edge(u,v)\n").split()
    a=int(a)
    b=int(b)
    g.addEdge(a, b)
    g.addEdge(b,a)
    
w=int(input("enter source vertex\n"))
print ("Following is Bfs") 
g.DFS(w)
