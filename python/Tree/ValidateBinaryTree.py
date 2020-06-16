import sys

class TreeNode:
    def __init__(self, val:int=0, left:TreeNode=None, right:TreeNode=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def validateTree(self, root: TreeNode):
        def validateTree(root: TreeNode, smallest: int, biggest: int):
            if not root:
                return True
            
            return smallest < root < biggest and validateTree(root.left, smallest, root.val) and validateTree(root.right, root.val, biggest)

        return validateTree(root, -sys.maxsize, sys.maxsize)

    # iteration
    def validateTree2(self, root: TreeNode):
        if not root:
            return True

        stack = [(root, -sys.maxsize, sys.maxsize)]

        while len(stack) > 0:
            node, minvalue, maxvalue = stack.pop()

            if not node:
                continue

            if node.val >= maxvalue or node.val <= minvalue:
                return False

            stack.append((node.right, node.val, maxvalue))
            stack.append((node.left, minvalue, node.val))

        return True