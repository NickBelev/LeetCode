# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp_lists = []

            # Merge neighboring pairs of lists, l and r and repeat
            # Logarithmic reduction of size of number of lists, each iteration
            for i in range(0, len(lists), 2):
                l = lists[i]
                r = None # In case we're out of bounds when lists is odd length
                if i + 1 < len(lists):
                    r = lists[i + 1] # Else properly assign r
                
                # Merge l and r and save that list to merge with others
                # in future iterations
                temp_lists.append(self.merge2Lists(l, r))

            lists = temp_lists # Reassign lists, now half as long
        
        return lists[0] # Loop terminated when lists reached a length of 1
        # That is our mega-list of all elements sorted

    # This is also the solution to another problem, I priorly solved it in Java
    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Starting head to build our sorted list off of
        curr = dummy # curr is for iterating reference

        # Alternate between both lists, sorting them by manipulating next's
        while list1 and list2:
            # Lists are sorted so pick smaller of currently lined up values
            # And increment respective list, assign proper next, increment curr
            # to continue sorting
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Ran out of list2 case
        if list1:
            curr.next = list1 # From where we left off in list1 in prior loop
        
        if list2: # Ran out of list1 case
            curr.next = list2 # From where we left off in list1 in prior loop
        
        return dummy.next # the head of the sorted (list1 + list2)
