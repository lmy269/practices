from typing import List
import heapq 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(first, last):
            return [TreeNode(root, left, right)
                        for root in range(first, last + 1)
                            for left in generateTrees(first, root - 1)
                                for right in generateTrees(root + 1, last)]
        return generateTrees(1, n)
