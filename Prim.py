class Graph :
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def printMST(self, parent): 
        sum=0
        print("Edge \tWeight")
        for i in range(1,self.V): 
            print(parent[i]+1,"-",i+1,"\t",self.graph[i][parent[i]])
            sum+=self.graph[i][parent[i]]
        print('Total min cost=',sum)
    def minKey(self, dist, mstSet):  
        min = float('Inf')
        min_index=-1
        for v in range(self.V): 
            if dist[v] < min and mstSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
    def primMST(self): 
        dist = [float('Inf')] * self.V 
        parent = [None] * self.V 
        dist[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1 
        for cout in range(self.V): 
            u = self.minKey(dist, mstSet) 
            mstSet[u] = True 
            for v in range(self.V):  
                if self.graph[u][v] > 0 and mstSet[v] == False and dist[v] > self.graph[u][v]: 
                        dist[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent) 
n=int(input('Enter the number of vertices\n')) 
v=int(input('Enter the number of edges\n'))
g = Graph(n) 
for i in range(v):
    u,v,cost=input('Enter edge(u,v) and cost:\n').split()
    u=int(u)-1
    v=int(v)-1
    cost=int(cost)
    g.graph[u][v]=cost
    g.graph[v][u]=cost
g.primMST(); 
