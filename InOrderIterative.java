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
        // Return list of integers, traversed in-order
        List<Integer> order = new ArrayList<>();
        // Stack to simulate recursive function call stack
        List<TreeNode> stack = new ArrayList<>();
        
        // We've only looked over the entire tree if both the current node is null
        // and there is no node on the stack that we have forgotten to visit
        while (!stack.isEmpty() || root != null) {
            // First traverse as left as possible, appending each visited node to the stack
            while (root != null) {
                stack.add(root);
                root = root.left;
            }
            // Once we can't go left anymore, we pop the last-added node from the stack
            // and append its value to our return order
            root = stack.remove(stack.size() - 1);
            order.add(root.val);
            // We then set up to descend left allong the right subtree, using this node
            root = root.right;
            // This is the crux of in-order: left subtree comes first, then we ascend to the parent,
            // Lastly we in-order traverse the right subtree
        }

        return order;
    }

}
