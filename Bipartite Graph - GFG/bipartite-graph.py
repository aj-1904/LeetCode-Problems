class Solution:
    # Bipartite Graph using BFS
    def bipartiteBFS(self, src, adj, color):
        queue = []
        # add src node to queue
        queue.append(src)
        # initially color src node with either 0 or 1
        color[src] = 1
        
        while queue:
            node = queue.pop(0)
            # traverse for adjacent node
            for adjacent_nodes in adj[node]:
                if color[adjacent_nodes] == -1:
                    # set up opposite color of adjacent node
                    color[adjacent_nodes] = 1 - color[node]
                    queue.append(adjacent_nodes)
                    # if the adjacent_node is already visited and has same color as of node, ret False
                elif color[adjacent_nodes] == color[node]:
                    return False
        return True
	def isBipartite(self, V, adj):
		#code here
        # color array of V size		
		color = [-1] * V
		for i in range(V):
		    if color[i] == -1:
		        if not self.bipartiteBFS(i, adj, color):
		            return False
		return True
		

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends