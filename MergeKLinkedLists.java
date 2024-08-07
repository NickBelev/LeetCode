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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null; // annoying guard clause

        ListNode list = lists[0]; // starts out as the head of the first list in lists,
        // which links to the rest of the list at lists[0]

        for (int i = 1; i < lists.length; i++) {
            list = mergeTwoLists(list, lists[i]); // Assign list a new head if
            // necessary, while merging the ith list into our megalist, list
        }

        return list; // We've merged all the lists together
    }

    // Solution to a prior question
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Create a dummy head for the result list
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        // Iterate through both lists
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        // Append the remaining elements of the non-exhausted list
        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        // Return the merged list, skipping the dummy head
        return dummy.next;
    }
}

