from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, result = [], [-1] * len(nums)
        
        for j in range(0, 2):
            for i, value in enumerate(nums):
                while stack and nums[stack[-1]] < value:
                    removed = stack.pop()
                    result[removed] = value

                stack.append(i)
                
        return result