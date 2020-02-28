from collections import defaultdict 
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        visited = [False] * (len(self.graph)) 
        queue = []  
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ")  
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
 
q=int(input('enter no. of edges'))
print()
g = Graph()
for i in range(q):
    a,b=input("enter edge(u,v)").split()
    print()
    a=int(a)
    b=int(b)
    g.addEdge(a, b) 
    

w=int(input("enter source vertex"))
print()
print ("Following is Bfs") 
g.BFS(w)
