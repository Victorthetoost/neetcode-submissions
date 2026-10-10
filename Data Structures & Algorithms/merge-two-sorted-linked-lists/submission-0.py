# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            ret = list1
            list1 = list1.next
        else:
            ret = list2
            list2 =list2.next    
        head = ret
        while list1 is not None and list2 is not None:
            print(ret.val,list1.val, list2.val)
            if list1.val < list2.val:
                print(ret.val, list1.val, list2.val)
                ret.next = list1
                ret = ret.next
                list1 = list1.next
            else:
                ret.next = list2
                ret = ret.next
                list2 =list2.next

        if list1 is None and list2 is not None:
            ret.next = list2
        elif list2 is None and list1 is not None:
            ret.next = list1
        return head

