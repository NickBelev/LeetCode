/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null; // Edge case

        Map<Integer, Node> vMap = new HashMap<>(); // Map for tracking visited nodes, and creating fresh copies of them

        List<Node> vStack = new ArrayList<>(); // Stack to traverse the graph in a BFS
        vStack.add(node); // Starting node to begin the BFS
        vMap.put(node.val, new Node(node.val)); // Create a fresh copy of the starting node

        // BFS Loop; terminates with correctness given a connected graph
        while (!vStack.isEmpty()) {
            Node curr = vStack.remove(vStack.size() - 1); // Pop current node from the stack, as it has been visited
            for (Node neighbor : curr.neighbors) { // Iterate through current node's neighbors
                if (!vMap.containsKey(neighbor.val)) {
                    // If we haven't encountered this neighbor yet, add it to the stack to visit
                    // Also, create a fresh copy of the neighbor, since we haven't yet
                    vStack.add(neighbor);
                    vMap.put(neighbor.val, new Node(neighbor.val));
                }
                // Accessing the fresh copy, of the currently visited node
                // Add all its neighbor copies to its adjacency list
                // We don't need to visit this node again
                vMap.get(curr.val).neighbors.add(vMap.get(neighbor.val));
            }
        }
        return vMap.get(node.val);
    }
}
