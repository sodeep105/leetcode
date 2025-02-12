# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        leftprev, curr = dummyHead, head
        for i in range(left-1):
            leftprev = curr
            curr = curr.next
        
        prev = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp      
        
        # dm -> 1 -> 2 <- 3 <- 4 <-5

        leftprev.next.next = curr
        leftprev.next = prev
        return dummyHead.next