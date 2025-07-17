# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_height = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.max_height = max(self.max_height,left+right)

            return 1 + max(left,right)
        
        height(root)
        return self.max_height
