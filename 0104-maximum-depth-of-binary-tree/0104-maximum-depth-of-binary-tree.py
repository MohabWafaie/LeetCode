# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        stack = [root]
        n = 0
        m = 0
        while(stack):
            current = stack[-1]
            if (current.left == None and current.right == None):
                stack.pop()
                n -= 1
            elif (current.left):
                stack.append(current.left)
                current.left = None
                n += 1
            else:
                stack.append(current.right)
                current.right = None
                n += 1
            m = max(m, n)
        return m + 1

        