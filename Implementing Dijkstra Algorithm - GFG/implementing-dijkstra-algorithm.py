import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        '''We will use pq(dis, node) and it will be min-heap such that node with lower distance 
        should be at top of priority queue'''
        
        distance = [float('inf')] * V
        distance[S] = 0
        
        pq = [] * (V+1)
        heapq.heappush(pq,(0, S))
        
        
        while pq:
            current_dis, current_node = heapq.heappop(pq)
            
            for neighbour in adj[current_node]:
                nextdis = neighbour[1]
                nextnode = neighbour[0]
                
                if current_dis + nextdis < distance[nextnode]:
                    distance[nextnode] = current_dis + nextdis
                    heapq.heappush(pq,(distance[nextnode], nextnode))
        return distance
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends