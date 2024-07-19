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
    public ListNode deleteDuplicates(ListNode head) {
        // Empty list is sorted trivially and free of duplicates
        if (head == null) return null;

        // Our pointers for two consecutive elements in the duplicate-free list
        ListNode fst = head;
        ListNode snd = head.next;

        // while the second pointer is not yet at the end of the list
        while (snd != null) {
            // if the first and second nodes have different values
            if (fst.val != snd.val) {
                // make the second node come directly after the first one
                // works since this list is sorted
                fst.next = snd;
                fst = fst.next; 
            // reposition the first pointer to come after the verified sublist
            }
            snd = snd.next;
            // whether or not snd is a duplicate of fst, this was dealt with
            // above, so just move snd one over to keep checking
        }

        // The above loop algorithm will not catch the case where the final
        // stretch of the sublist is all duplicates. Ex. 12344 as snd will keep
        // being incremented until it is null so we do a final check that the
        // node after fst is not a duplicate; if it is, it means every node
        // until the end after fst is a duplicate of fst, so we remove the 
        // remainder of the list
        // If this is not the case thought, fst will end up assigned to the 
        // last node in the list, so fst.next would be null, which is how
        // we know to avoid this check
        if (fst.next != null && fst.val == fst.next.val) {
            fst.next = null;
        }

        return head;
    }
}
