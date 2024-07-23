# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def treeBuild(l, r):
            if l > r: # We've covered every index between l and r
                return None # Base case
            mid = (l + r) // 2 # Like binary search algorithm
            # Node of the current level should always be middle of the search zone
            root = TreeNode(nums[mid])
            root.left = treeBuild(l, mid - 1) # Recursively build left subtree
            root.right = treeBuild(mid + 1, r) # Same for right subtree

            return root # Root of the whole tree once all recursion is done

        return treeBuild(0, len(nums) - 1)
