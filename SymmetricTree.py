# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # Both nodes we have recursed down towards are null, base case
            if not p and not q:
                return True
            # One of the nodes is null but not both, means the trees can't mirror as 
            # we've noticed a difference in their traversal so end the
            # recursion right then and there
            if not p or not q:
                return False

            # Else we check that the current node's values are equal and 
            # recursively continue this check for the left and right subtrees
            # of p and q respectively, but in flipped order to check that they
            # mirror each other
            return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
        
        # A null tree is symmetric trivially
        if not root:
            return True

        return isMirror(root.left, root.right)

        
