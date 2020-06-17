from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        isVisited = [0]*numCourses
        graph = [[] for i in range(numCourses)]

        for node, dep in prerequisites:
            graph[node].append(dep)
            
        def dfs(node: int) -> bool:
            if isVisited[node] == 1:
                return True
            if isVisited[node] == 2:
                return False
            
            isVisited[node] = 2
            
            for child in graph[node]:
                if not dfs(child):
                    return False
            isVisited[node] = 1
            return True
        
        for value in range(numCourses):
            if not dfs(value):
                return False
            
        return True