class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print("==========")
        first = head
        second = head

        for i in range(n):

            if second.next == None:
                if i == n - 1:
                    head = head.next
                return head

            second = second.next        

        while second.next != None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return head