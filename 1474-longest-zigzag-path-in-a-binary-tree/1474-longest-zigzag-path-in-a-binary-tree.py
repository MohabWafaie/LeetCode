# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, "root", 0)
    def helper(self, root, d, count):
        count = count
        if d == "right":
            if root.left:
                count += 1
                count = max(self.helper(root.left, "left", count), count)
            if root.right:
                count = max(self.helper(root.right, "right", 1), count)
        elif d == "left":
            if root.right:
                count += 1
                count = max(self.helper(root.right, "right", count), count)
            if root.left:
                count = max(self.helper(root.left, "left", 1), count)
        elif d == "root":
            if root.left:
                count = max(self.helper(root.left, "left", 1), count)
            if root.right:
                count = max(self.helper(root.right, "right", 1), count)
        return count
        