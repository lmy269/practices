import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int)
        start, maxcount, maxlength = 0, 0, 0
        
        for i, value in enumerate(s):
            counts[value] += 1
            maxcount = max(maxcount, counts[value])
            
            if i - start + 1 - maxcount > k:
                counts[s[start]] -= 1
                start += 1
            
            maxlength = max(maxlength, i - start + 1)
            
        return maxlength
        