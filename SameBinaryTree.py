# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes we have recursed down towards are null, base case
        if not p and not q:
            return True
        # One of the nodes is null but not both, means the trees can't be the 
        # same, as we've noticed a difference in their traversal so end the
        # recursion right then and there
        if not p or not q:
            return False

        # Else we check that the current node's values are equal and 
        # recursively continue this check for the left and right subtrees
        # of p and q respectively
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
