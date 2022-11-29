# O(n) O(1)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = [0, 0]
        for s in students:
            cnt[s] += 1
        for s in sandwiches:
            if cnt[s] == 0:
                break
            cnt[s] -= 1
        return cnt[0] + cnt[1]

# # O(n^2) O(n)
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         q = deque(students)
#         i = 0
#         cnt = 0
#         while q and cnt < len(q):
#             if q[0] == sandwiches[i]:
#                 q.popleft()
#                 i += 1
#                 cnt = 0
#             else:
#                 q.append(q.popleft())
#                 cnt += 1
#         return len(q)
