# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow and fast pointer and if at some point slow pointer == fast pointer, then there is a cycle

        # what is a slow pointer
        # -- slow pointer traverses list at one step at a time

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False