from collections import defaultdict  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
           
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0  
        e = 0
        
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = []
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)
                
        print("Following are the edges in the constructed MST")
        for u,v,weight  in result:  
            print ("%d -- %d == %d" % (u+1,v+1,weight))
nov=int(input('Enter the number of vertices\n'))
noe=int(input('Enter the number of edges\n'))
g=Graph(nov)
for i in range(noe):
    u,v,cost=input('Enter edge(u,v) and its cost\n').split()
    u=int(u)-1
    v=int(v)-1
    cost=int(cost)
    g.addEdge(u,v,cost)
    g.addEdge(v,u,cost)
g.KruskalMST()
