# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # No root means no pairs
        if not root:
            return 0

        self.good_pairs = 0 # counter for satisfactory leaf pairs

        # Search the tree recursively and determine satisfactory pairs at each
        # level, when the search is finished, good_pairs will have the correct
        # value
        self.traverse_dfs(root, distance)

        return self.good_pairs

    # Recursive helper to smartly count pairs
    def traverse_dfs(self, node, dist):
        # Null tree
        if not node:
            return [] # Empty list of distances from leaves

        # We're at a leaf
        if not node.left and not node.right:
            return [1] # Returns 1 to the node that called this leaf
            # So the parent knows that it is 1 dist away from a leaf

        # Recursively continue traversal to reach leaves
        left_leaf_dists = self.traverse_dfs(node.left, dist)
        right_leaf_dists = self.traverse_dfs(node.right, dist)

        # Using the left and right distances of leaves from the current node
        # Check for all combinations of these leaf distances if adding them
        # AKA going from left leaf to node right leaf (or the reverse) yields
        # a distance less than the permitted amount
        for l_d in left_leaf_dists:
            for r_d in right_leaf_dists:
                if l_d + r_d <= dist:
                    self.good_pairs += 1 # Found a satisfactory leaf pair
        # The above segment is only accessible after leaves are first reached, 
        # via the order of return statements, so pairs are checked on the ascent
        # back up the tree since after each ascension, the formerly left and
        # right children of the previous parent are grouped as either left or
        # right children of the higher-up parent node--meaning those pairs will
        # not be cross-checked against each other again--property of Binary Tree

        # We're returning this to the parent which means we merge the left and
        # right leaf distances of the current node and increment them all by 1
        # this happens in the recursive calls ascending, after having reached
        # the leaves and worked up, checking pairs for all the descendants
        return [1 + concatd_dis for concatd_dis in (left_leaf_dists + right_leaf_dists)]


        

