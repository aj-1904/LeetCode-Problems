class Solution:
    
    #Function to return list containing vertices in Topological order.
    # def findTopoSort(self, node, vis, stack, adj):
    #     # using DFS
    #     vis[node] = 1
        
    #     for neighbour in adj[node]:
    #         if not vis[neighbour]:
    #             self.findTopoSort(neighbour, vis, stack, adj)
    #     stack.append(node)
        
    
    # def topoSort(self, V, adj):
    #     # Code here
    #     stack = []
    #     vis = [0] * N
        
    #     for i in range(N):
    #         if not vis[i]:
    #             self.findTopoSort(i, vis, stack, adj)
        
    #     topo = []
    #     while stack:
    #         topo.append(stack.pop())
    #     return topo
    def topoSort(self, V, adj):
        # using BFS(Kahn's Algorithm)
        
        queue = []
        indegree = [0] * V
        
        for i in range(V):
            for neighbour in adj[i]:
                indegree[neighbour] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        topo = []
        while queue:
            node = queue.pop(0)
            topo.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return topo


#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends