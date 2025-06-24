# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()
        current = head
        while current!=None:
            queue.append(current)
            current=current.next
        head = queue.popleft()
        use_tail = True
        dummy = head 
        while queue:
            if use_tail:
                element = queue.pop()
            else:
                element = queue.popleft()

            dummy.next = element
            dummy = element
            use_tail = not use_tail
        dummy.next = None
