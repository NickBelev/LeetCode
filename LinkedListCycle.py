# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one, two = head, head
        
        while two and two.next:        
            one = one.next # Slow pointer moves by one on the LL
            two = two.next.next # Fast pointer moves by two
            # If there'es a cycle eventually both will get trapped going in circles
            # However, slow moves by 1 and fast moves by 2, so even though
            # fast is ahead of slow, if there is a cycle, their relative 
            # distance decreases by 1 each iteration until the fast pointer
            # catches back up to the slower moving one

            # This can only happen if there's a cycle
            if one == two:
                return True
        
        return False # Otherwise we reached a null => no cycle
        
