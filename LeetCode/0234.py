# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

# # O(n) O(n)
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         vals = []
#         cur = head
#         while cur:
#             vals.append(cur.val)
#             cur = cur.next
#         return vals == vals[::-1]
