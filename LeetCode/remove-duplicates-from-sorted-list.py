from typing import ListNode,Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = head
        #prev.next = None
        t = head
        while True:
            if t==None:
                break
            if t.val != prev.val:
                prev.next = t
                prev = t
            t = t.next
        
        prev.next = None
        return head