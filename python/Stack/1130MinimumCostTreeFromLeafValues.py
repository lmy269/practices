from typing import List
import sys

class Solution:

    # remove the smallest value until i from the stack
    # cost is smallest * min(left, right)
    # until only 1 left
    # with sys.maxsize, we don't need to check length
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack, res = [sys.maxsize], 0
        
        for value in arr:
            while stack[-1] <= value:
                removed = stack.pop()
                res += removed * min(value, stack[-1])
            stack.append(value)
        
        while len(stack) > 2:
            removed = stack.pop()
            res += removed * stack[-1]
            
        return res
        