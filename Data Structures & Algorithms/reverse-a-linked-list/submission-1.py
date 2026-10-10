# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if head.next == None:
            return head
        curr = head
        head = curr.next
        curr.next = None
        prev = curr
        while head.next != None:
            curr = head
            head = curr.next
            curr.next = prev
            prev = curr
        curr = head
        curr.next = prev
        return head

        