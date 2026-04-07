# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            
        if p and q:
            if p.val!=q.val:
                return False
            else:
                leftp,leftq=p.left, q.left
                rightp,rightq=p.right,q.right

                return self.isSameTree(leftp, leftq) and self.isSameTree(rightp,rightq)

        elif not p and not q:
            return True
        else:
            return False
        
        
        
        