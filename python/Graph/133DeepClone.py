class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cache = {}

        def clone(node: Node):
            if node not in cache:
                newNode = cache[node] = Node(node.val)
                newNode.neighbors = list(map(clone, node.neighbors))
                return newNode
            return cache[node]

        return node and clone(node)