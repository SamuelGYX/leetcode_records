'''
Overview:

    Detect whether there is loop in a direct graph.

Solution:

    DFS with enhanced visit:

        0: haven't visited
        
        1: is currently tracking along this vertex
        
        2: exploited, we have visited this vertex and all of its successors, no loop
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        
        for u, v in prerequisites:
            graph[u].append(v)
            
        def dfs(x):
            if visit[x] == 1:
                return True
            if visit[x] == 2:
                return False
            visit[x] = 1
            for y in graph[x]:
                if dfs(y):
                    return True
            visit[x] = 2
            return False
            
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True