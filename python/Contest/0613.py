import unittest
from typing import List
import math

class Solution(unittest.TestCase):
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[i - 1] + nums[i])

        return result

    def test_runningSum(self):
        self.assertEqual(self.runningSum([3,1,2,10,1]), [3,4,6,16,17])

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cache = {}
        for value in arr:
            if value not in cache:
                cache[value] = 0
            cache[value] += 1

        sortedCounts, removedCount = sorted(cache.values()), 0
        
        while k > 0:
            if k >= sortedCounts[removedCount]:
                k -= sortedCounts[removedCount]
                removedCount += 1
            else:
                k = 0
        
        return len(cache.keys()) - removedCount


    def test_findLeastNumofUniqueInts(self):
        self.assertEqual(self.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3), 2)

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        cache = {}
        for value in bloomDay:
            if value not in cache:
                cache[value] = 0
            cache[value] += 1
        sortedDays = sorted(cache.keys())
        mindays, left, right = 0, 0, len(sortedDays) - 1

        def mBouquets(day: int):
            current, total = 0, 0
            for value in bloomDay:
                if value <= day:
                    current += 1
                    if current == k:
                        total += 1
                        current = 0
                        if m == total:
                            return True

            return False

        while left <= right:
            mid = (left + right) // 2
            if mBouquets(mid):
                mindays = sortedDays[mid]
                right = mid - 1
            else:
                left = mid + 1
        return mindays

    def test_minDays(self):
        self.assertEqual(self.minDays([1,10,2,9,3,8,4,7,5,6], 4, 2), 9)

    # binary lift
    # construct table up[i][j] = node after i jumps 2^j
    # up[i][j] = up[up[i][j - 1]][j - 1]
    class TreeAncestor:

        def __init__(self, n: int, parent: List[int]):
            self.n = n
            self.parent = parent
            self.totaljump = int(math.log(n)//math.log(2))
            self.up =[[-1] * (self.totaljump + 1) for i in range(len(parent))]
            
            for i in range(len(parent)):
                self.up[i][0] = parent[i]
                
            for i in range(1, len(parent)):
                for j in range(1, (self.totaljump + 1)):
                    if (self.up[i][j - 1] != -1):
                        self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]                    
            

        def getKthAncestor(self, node: int, k: int) -> int:
            if k >= self.n:
                return -1
            
            for i in range(self.totaljump, -1, -1):
                if k & 1 << i:
                    node = self.up[node][i]
                    if node == -1:
                        return -1
                    k -= 1 << i
                
            return self.up[node][0] if k > 0 else node

    def testGetKthAncestor(self):
        tree = self.TreeAncestor(7, [-1,0,0,1,1,2,2])
        self.assertEqual(tree.getKthAncestor(3, 1), 1)
        self.assertEqual(tree.getKthAncestor(5, 2), 0)
        self.assertEqual(tree.getKthAncestor(6, 3), -1)

if __name__ == "__main__":
    unittest.main()
