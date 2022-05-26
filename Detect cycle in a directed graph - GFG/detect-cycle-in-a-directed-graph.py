#User function Template for python3

# Detect Cycle in Directed Graph(using DFS)
class Solution:
    
    def checkCycleDFS(self, node, adj, vis, dfsVis):
        # mark starting node as visited in both vis and dfsVis
        vis[node] = 1
        dfsVis[node] = 1
        
        # traverse for adjacent nodes
        for adjacent_node in adj[node]:
            # if adjacent_node is not visited
            if not vis[adjacent_node]:
                # call function with adjacent node
                if self.checkCycleDFS(adjacent_node, adj, vis, dfsVis):
                    return True
            # if already visted and dfsVis also visted
            elif dfsVis[adjacent_node] == 1:
                return True
        # if no cycle found then mark node as unvisted in dfsVis again
        dfsVis[node] = 0
        return False
            
    
    
    #Function to detect cycle in a directed graph.
    
    def isCyclic(self, V, adj):
        # code here
        vis = [0] * V
        dfsVis = [0] * V
        
        for i in range(0, V):
            if not vis[i]:
                if self.checkCycleDFS(i, adj, vis, dfsVis):
                    return True
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends