# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            self.stack = []
            self.helper(root, 0, 0)
            return self.stack
    stack = []
    def helper(self, root, max_node, current):
        if (not root):
            return None
        if current == 0 or current > max_node:
            self.stack.append(root.val)
            max_node = current
        if root.right:
            max_node = self.helper(root.right, max_node, current + 1)
        if root.left:
            max_node = self.helper(root.left, max_node, current + 1)
        return max_node
        

        
