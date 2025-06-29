# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while (head):
            l.append(head)
            head = head.next
        length = len(l)
        l[int(length/2) - 1].next = l[int(length/2) + 1] if length > 2 else None
        if(len(l) == 1):
            l[0] = l[0].next
        return l[0]
        
        