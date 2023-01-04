# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res

# # O(n) O(n)
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         s = ''
#         while head:
#             s += str(head.val)
#             head = head.next
#         return int(s, 2)
