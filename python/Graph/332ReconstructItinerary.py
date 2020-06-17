import collections
from typing import List

class Solution:

    # DFS until to the end, add the node to route
    # Adding no dependenies nodes into route when retreating
    # Loop sub paths when the node has other dependencies
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        stack, route = ['JFK'], []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        
        return route[::-1]