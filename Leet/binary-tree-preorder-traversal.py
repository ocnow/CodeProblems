# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = []
        stack.append(root)
        ans = []

        while len(stack) != 0:
            tp = stack.pop()
            ans.append(tp.val)

            if tp.right is not None:
                stack.append(tp.right)
            if tp.left is not None:
                stack.append(tp.left)
        
        return ans
