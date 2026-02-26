# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        The Problem: Reorder a singly-linked list such that it alternates between the first node, last node, second node, second-to-last node, and so on (e.g., L0 → Ln → L1 → Ln-1 → ...).
        
        The Core Problem: Rearrange the nodes by interleaving the first half of the list with the reversed second half, without modifying node values.
        
        The SubProblems:
        1. How to find the middle of the list to split it into two halves?
           - Use two pointers (slow and fast) to locate the middle node.
        2. How to reverse the second half of the list?
           - Reverse the links of the nodes starting from the middle to the end.
        3. How to merge the first half with the reversed second half?
           - Interleave nodes by alternating between the first half and the reversed second half.
        4. How to handle edge cases like lists with one or two nodes?
           - Check if the list is too short to reorder, in which case no changes are needed.
        """
        # Subproblem 4: Handle edge cases (list with 1 or 2 nodes)
        if not head or not head.next:
            return
        
        # Subproblem 1: Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Subproblem 2: Reverse the second half
        second_half = slow.next
        slow.next = None  # Split the list
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        
        # Subproblem 3: Merge the first half with the reversed second half
        first = head
        second_half = prev
        while second_half:
            temp1, temp2 = first.next, second_half.next
            first.next, second_half.next = second_half, temp1
            first, second_half = temp1, temp2
        
        