# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


# # O(n) O(1)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         s = f = head
#         while f and f.next:
#             s = s.next
#             f = f.next.next
#             if s == f:
#                 return True
#         return False
