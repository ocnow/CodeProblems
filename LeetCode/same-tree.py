# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.printInorder(p,q)

    def printInorder(self, p,q):
        
        if p == None:
            if q!=None:
                return False
            
            if q == None:
                return True
            
        if p != None:
            if q == None:
                return False

            if q.val != p.val:
                return False
        

        if not self.printInorder(p.left,q.left) or not self.printInorder(p.right,q.right):
            return False

        return True