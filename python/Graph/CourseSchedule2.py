from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        visited = [0]*numCourses
        graph = [[] for i in range(numCourses)]
        
        for node, dep in prerequisites:
            graph[dep].append(node)

        def dfs(node: int) -> bool:
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 2
            
            for child in graph[node]:
                if not dfs(child):
                    return False
            visited[node] = 1
            stack.append(node)
            return True
        
        for node in range(numCourses):
            if visited[node] == 1:
                continue
            if not dfs(node):
                return []
            
        return reversed(stack)
        