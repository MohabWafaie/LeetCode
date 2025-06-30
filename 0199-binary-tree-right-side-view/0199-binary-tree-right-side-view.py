# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def helper(root, current):
            if (not root):
                return None
            if current == len(stack):
                stack.append(root.val)
            if root.right:
                max_node = helper(root.right, current + 1)
            if root.left:
                max_node = helper(root.left, current + 1)
        helper(root, 0)
        return stack
        
        

        
