# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        if head.next == None:
            return head
        #print("===============")
        tip = head
        toe = tip.next
        prev = None

        retHead = toe
        

        while tip!= None and toe != None:
            #print("testing---")
            tip.next = toe.next
            toe.next = tip

            if prev != None:
                prev.next = toe

            prev = tip

            tip = tip.next
            if tip!= None:
                toe = tip.next

            #self.printList(retHead)
        return retHead
        