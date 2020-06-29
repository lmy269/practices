from typing import List
import collections
from collections import deque
import unittest

class Solution(unittest.TestCase):
    def getFolderNames(self, names: List[str]) -> List[str]:
        cache = collections.defaultdict(int)
        cacheDeque = collections.defaultdict(deque)
        output = []
        
        for value in names:
            if cache[value] > 0:
                while cacheDeque[value] and cacheDeque[value][0] <= cache[value] + 1:
                    na = cacheDeque[value].popleft()
                    if na == cache[value] + 1:
                        cache[value] += 1
                output.append(value + f'({cache[value]})')
                cache[value] += 1
            else:
                cache[value] += 1
                output.append(value)
            
            if value.endswith(')'):
                values = value.split('(')
                if len(values) > 1:
                    suffixNum = values[-1][0:-1]
                    try:
                        index = int(suffixNum)
                        realvalue = value[0:-(len(values[-1])+1)]
                        cacheDeque[realvalue].append(index)
                    except ValueError:
                        continue

                        
        return output

    def test_case1(self):
        self.assertEqual(self.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]), ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"])
                
        
if __name__ == "__main__":
    unittest.main()