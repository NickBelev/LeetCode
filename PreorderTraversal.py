# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Null root guard
        if not root:
            return []

        # For the DFS
        stack = []
        # For the visiting order
        traversal = []
        stack.append(root) # Start DFS on root of tree

        while stack:
            node = stack.pop()
            # If node is null, just ignore it, our work is done
            # It doesn't affect traversal order
            if node:
                traversal.append(node.val) # "Visit"
                # Order matters, always want to visit left first, so have it on
                # top to pop first
                stack.append(node.right)
                stack.append(node.left)
        
        return traversal
        
