# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0, head)
        slow = dummyhead
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                slow.next = head
            else:
                slow = head
                head = head.next
        
        return dummyhead.next

        