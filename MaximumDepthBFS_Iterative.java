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
        if (root == null) return 0;

        // Stacks for traversing the tree and mirroring the traversal wih discovered depths
        List<TreeNode> visitStack = new ArrayList<>();
        List<Integer> depthStack = new ArrayList<>();

        visitStack.add(root);
        depthStack.add(1);
        int maxDepthDFS = 1; // Since we have a root, the depth of it is 1

        // We discover the depth of every node by visiting each node with a pre-order traversal
        while (!visitStack.isEmpty()) {
            TreeNode visited = visitStack.remove(visitStack.size() - 1); // pop the node to visit
            int currDepth = depthStack.remove(depthStack.size() - 1); // pop to find out that node's depth

            if (visited != null) { // if the node we popped exists, we check its depth to see if it's bigger than
                // any depth yet discovered
                maxDepthDFS = Math.max(maxDepthDFS, currDepth);
                visitStack.add(visited.left); // prepare both children for visiting shortly after
                visitStack.add(visited.right);
                // If one of these added children is null,
                // this condition clause won't run for them
                // so will not affect the max depth tracking / calculation
                depthStack.add(currDepth + 1); // both children will have a depth greater than the parent by 1, if they're not null
                depthStack.add(currDepth + 1);
            }
        }
        return maxDepthDFS; // the max depth found after traversing every node in the BST
    }
}
