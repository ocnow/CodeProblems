from typing import Optional,ListNode
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        #go till k
        t = head
        le = 0
        while k > 0:
            t = t.next
            k = k - 1
            le = le + 1
            if t == None:
                k = k % le
                t = head
            
        
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
        if q == None:
            return head
        p.next = None
        backupq = q
        #print("q val"+str(q.val))

        while q.next != None:
            q = q.next

        q.next = head
        return backupq