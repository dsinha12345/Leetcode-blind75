# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h1 = []
        for ll in lists:
            while ll:
                heapq.heappush(h1,ll.val)
                ll=ll.next
        res = ListNode()
        curr = res
        while h1:
            curr.next = ListNode(heapq.heappop(h1))
            curr = curr.next
        return res.next
