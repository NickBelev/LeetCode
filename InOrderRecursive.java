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

    public List<Integer> inorderTraversal(TreeNode root) {
        // Create a return list accumulator
        List<Integer> order = new ArrayList<>();
        // Run the helper function
        inOrderRec(root, order);
        return order;
    }

    // Functional programming inspired accumulator approach
    private void inOrderRec(TreeNode curr, List<Integer> order) {
        // Base case: if the current node is null, return this recursive branch as it is done
        if (curr == null) return;
        
        // Traverse left subtree
        inOrderRec(curr.left, order);
        
        // Add the current node to our traversal list, in order
        order.add(curr.val);
        
        // Traverse right subtree
        inOrderRec(curr.right, order);
    }

}
