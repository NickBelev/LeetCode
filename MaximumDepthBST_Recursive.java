/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0; // Base case, no where deeper to go
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right)); // Subproblems:
      // Go one level down to determine the depth of the left and right subtrees, do this recursively
      // upon reaching the base of each recursive branch, we recurse upwards, max(max(...), max(...)) will pick
      // the longest branch at each subtree, and we keep adding 1 as we go back up and repeat until we reach the initial root
      // returning the height of the whole tree
    }
}
