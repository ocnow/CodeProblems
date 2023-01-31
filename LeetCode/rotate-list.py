# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #go till k
        t = head
        for i in range(k):
            t = t.next
        
        #print("t at:"+str(t.val))
        #backupk = t

        #take another pointer and move forward till t is null
        p = head
        while t.next!= None:
            #print("t at:"+str(t.val))
            #print("p at:"+str(p.val))
            p = p.next
            t = t.next

        #print("p valt"+str(p.val))
        q = p.next
        p.next = None
        backupq = q
        #print("q val"+str(q.val))

        while q.next != None:
            q = q.next

        q.next = head
        return backupq