# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.calc(root) + 1
    def calc (self, root):
        if(not root):
            return 0
        n = 0
        if root.left:
            if root.left.val >= root.val:
                n += 1
            else :
                root.left.val = root.val
        if root.right:
            if root.right.val >= root.val:
                n += 1
            else :
                root.right.val = root.val
        n += self.calc(root.left)
        n += self.calc(root.right)
        return n
        
        
        