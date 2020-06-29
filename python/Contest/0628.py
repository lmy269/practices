from typing import List
import sys
import collections

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0, 0)
        cache = set()
        cache.add(current)
        
        for value in path:
            if value == 'N':
                current = (current[0], current[1] + 1)
            elif value == 'S':
                current = (current[0], current[1] - 1)
            elif value == 'E':
                current = (current[0] + 1, current[1])
            else:
                current = (current[0] - 1, current[1])
        
            if current in cache:
                return True
            cache.add(current)
        
        return False

    def canArrange(self, arr: List[int], k: int) -> bool:
        cache = [0] * k
        
        for value in arr:
            cache[value % k] += 1
        
        for i, value in enumerate(cache):
            if (i == 0 or k == 2*i):
                if value % 2 != 0:
                    return False
            elif value != cache[k - i]:
                return False
            
        return True
        
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        deq = collections.deque()
        result = -sys.maxsize
        
        for x, y in points:
            while deq and x - deq[0][0] > k:
                deq.popleft()
            
            if deq:
                result = max(result, x + y + deq[0][1] - deq[0][0])
            
            while deq and ((deq[-1][1] - deq[-1][0]) < y - x):
                deq.pop()
            
            deq.append([x, y])
        
        return result
            