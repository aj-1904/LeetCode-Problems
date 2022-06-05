#User function Template for python3
import heapq
class Solution:
    # Prim's Algorithm
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        key = [float('inf')] * V
        inMST = [False] * V
        parent = [-1] * V
        
        pq = [] #(weight, node)
        heapq.heappush(pq, (0, 0)) #pushing weight 0 for src node and src node
        
        key[0] = 0
        
        while pq:
            current_weight, current_node = heapq.heappop(pq)
            inMST[current_node] = True
            
            for neighbour in adj[current_node]:
                next_weight = neighbour[1]
                next_node = neighbour[0]
                
                if inMST[next_node] == False and key[next_node] > next_weight:
                    key[next_node] = next_weight
                    heapq.heappush(pq, (key[next_node], next_node))
                    parent[next_node] = current_node
        return sum(key)
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends