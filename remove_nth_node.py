# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dict1 = {}
        i = 0
        while curr:
            dict1[i] = curr
            curr = curr.next
            i+=1
        prev = i-n-1
        if prev<0:
            return head.next
        if prev+2<i:
            dict1[prev].next = dict1[prev+2]
        else:
            dict1[prev].next = None
        return head

