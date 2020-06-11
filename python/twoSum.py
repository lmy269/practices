from typing import List
import unittest

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,value in enumerate(nums):
            if (target - value in cache):
                return [cache[target - value], i]
            cache[value] = i
        
        return None

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        indexes = self.solution.twoSum([1,2,3], 3)
        self.assertEqual(indexes, [0, 1])

if __name__ == "__main__":
    unittest.main()

