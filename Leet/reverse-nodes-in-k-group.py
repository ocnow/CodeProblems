#Referenced the youtube video: https://www.youtube.com/watch?v=1UOPsfP85V4

from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        prevKGroupEnd = dummy
        
        while True:
            kthNode = self.getKth(prevKGroupEnd,k)
            
            if not kthNode:
                break
            
            groupNext = kthNode.next
            
            #reverse process
            prev, curr = kthNode.next, prevKGroupEnd.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            #reverse done
            #store curr head in tmp
            tmp = prevKGroupEnd.next
            prevKGroupEnd.next = kthNode
            prevKGroupEnd = tmp
        return dummy.next

    def getKth(self,head,k):
        i = 0
        while head and i < k:
            head = head.next
            i = i + 1

        return head