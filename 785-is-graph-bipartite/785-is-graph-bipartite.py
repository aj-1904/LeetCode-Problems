class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        # adjList = self.buildAdjacencyList(graph)
        
        for i in range(0, n):
            if color[i] == -1:
                if not self.checkBipartiteBFS(i, graph, color):
                    return 0
        return 1

    def checkBipartiteBFS(self, src, graph, color):
        
        queue = []
        queue.append(src)
        color[src] = 1 #initially color src node with 0 or 1

        while queue:
            node = queue.pop(0)
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    queue.append(neighbour)
                elif color[neighbour] == color[node]:
                    return False
        return True

#     def buildAdjacencyList(self, edges):
#         adj = defaultdict(list) # a dict of list 
#         for x, y in edges:
#             adj[x].append(y)
#         return adj
        