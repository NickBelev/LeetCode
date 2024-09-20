# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
    
#         def dfs(root_state):
#             root, curr_max = root_state

#             if not root:
#                 return 0

#             curr_max = max(root.val, curr_max)

#             return dfs((root.left, curr_max)) + dfs((root.right, curr_max)) + (1 if root.val >= curr_max else 0)

#         if root:
#             return dfs((root, root.val))
#         return 0



class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        stack = [(root, root.val)]
        good_nodes = 0

        while stack:

            curr, curr_max = stack.pop()

            if curr.val >= curr_max:
                good_nodes += 1

            if curr.left:
                stack.append((curr.left, max(curr.val, curr_max)))
            if curr.right:
                stack.append((curr.right, max(curr.val, curr_max)))
        
        return good_nodes


            
