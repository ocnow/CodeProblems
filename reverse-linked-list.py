#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 4 -> 5 -> 6 -> None
        current = head
        last_node = None
        tmp = None
        while current != None:
            tmp = current.next
            current.next= last_node
            last_node = current
            current = tmp
        return last_node