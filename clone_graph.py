"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}
        def clone(node):
            if node in maps:
                return maps[node]
            clone_node = Node(node.val)
            maps[node] = clone_node
            for neighbors in node.neighbors:
                clone_node.neighbors.append(clone(neighbors))
            return clone_node
        return clone(node)
