from typing import List

class Solution:

    # BFS, remove leaves, new leaves until total length <= 2
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for i in range(n)]
        
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        
        leaves = []
        
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        while n > 2:
            newleaves = []
            for leave in leaves:
                parent = graph[leave].pop()
                graph[parent].remove(leave)
                n -= 1
                if len(graph[parent]) == 1:
                    newleaves.append(parent)
            
            leaves = newleaves
            
        return leaves
        