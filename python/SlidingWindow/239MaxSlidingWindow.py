import collections
from typing import List

class Solution:

    # deque (usually pronounced like "deck")
    # use a deque to maintain a max value list from left to right
    # update the deque remove all the old small value from right
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = collections.deque(), []
        
        for i, value in enumerate(nums):
            while queue and nums[queue[-1]] <= value:
                queue.pop()
            queue.append(i)
            
            if queue[0] < i - k + 1:
                queue.popleft()
            
            if i + 1 < k:
                continue
                
            result.append(nums[queue[0]])
            
        return result