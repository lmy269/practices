from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, i, j = 0, 0, len(height) - 1

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            maxarea = max(area, maxarea)
            if (height[i] > height[j]):
                j -= 1
            else:
                i += 1

        return maxarea