/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Only removable node is the head or nothing to remove at all
        if (head == null || head.next == null) return null; 
        
        // Count total number of nodes in the linked list
        int num_nodes = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            num_nodes++;
        }

        int remove_index = num_nodes - n; // where index 0 is the head

        if (remove_index == 0) return head.next; // Edge case that will misbehave and remove the node after the head instead of the head because of the condition on the below while loop

        // Count total number of nodes in the linked list
        int trav_count = 0;
        curr = head; // Start traversal from beginning
        while (trav_count < remove_index - 1) {
            curr = curr.next;
            trav_count++;
        }
        // curr now points to the node before the one that needs removing
        // So we simply skip over the node-to-remove
        curr.next = curr.next.next;
        return head;
    }
}
