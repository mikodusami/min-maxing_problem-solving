# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two Heads:
        state:
        - newly instantiated list (neil)
        - list1
        - list2
        transitions:
        do this while both list1 and list2 point to valid nodes
        - if list1.val < list2.val: neil.next = list1.val 
            - neil = neil.next
            - list1 = list1.next
        else:
            - neil = neil.next
            - list2 = list2.next
        
        since one of them will be None, we need to append the rest
        so if list1 is not null, we say neil.next = list1 (reference)
        """

        dummy = neil = ListNode() # at 0, None
        while list1 and list2:
            if list1.val < list2.val:
                neil.next = list1
                list1 = list1.next
            else:
                neil.next = list2
                list2 = list2.next
            neil = neil.next
        
        neil.next = list1 if list1 else list2
        return dummy.next