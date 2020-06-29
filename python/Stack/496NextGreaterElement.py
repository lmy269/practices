from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, cache = [], {}
        
        for value in nums2:
            while stack and stack[-1] < value:
                removed = stack.pop()
                cache[removed] = value
            
            stack.append(value)
            
        res = []
        
        for value in nums1:
            res.append(-1 if value not in cache else cache[value])
        
        return res