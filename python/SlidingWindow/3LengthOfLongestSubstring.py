class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache, start, longest = {}, 0, 0
        
        for i, value in enumerate(s):
            if value not in cache or cache[value] < start:
                longest = max(longest, i - start + 1)
            else:
                start = cache[value] + 1
            cache[value] = i
            
        return longest