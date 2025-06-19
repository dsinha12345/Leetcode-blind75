# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def valid_subtree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val!=node2.val:
                return False
            if node1.val == node2.val:
                return valid_subtree(node1.left,node2.left) and valid_subtree(node1.right, node2.right)
        
        if valid_subtree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)            
                                
