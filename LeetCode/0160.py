# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(m+n) O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt
        
        la, lb = length(headA), length(headB)
        a, b = headA, headB
        if la > lb:
            for _ in range(la - lb):
                a = a.next
        else:
            for _ in range(lb - la):
                b = b.next
        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
