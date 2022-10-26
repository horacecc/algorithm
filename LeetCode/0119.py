# O(n) O(n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        return row

# # O(n^2) O(n)
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [1] * (rowIndex + 1)
#         for i in range(2, rowIndex + 1):
#             for j in range(i - 1, 0, -1):
#                 row[j] += row[j - 1]
#         return row

# # O(n^2) O(n)
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [1]
#         for i in range(1, rowIndex + 1):
#             new_row = [1]
#             for j in range(1, i):
#                 new_row.append(row[j-1] + row[j])
#             new_row.append(1)
#             row = new_row
#         return row

# # O(n^2) O(n^2)
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         triangle = [[1]]
#         for i in range(1, rowIndex + 1):
#             row = [1]
#             for j in range(1, i):
#                 row.append(triangle[i-1][j-1] + triangle[i-1][j])
#             row.append(1)
#             triangle.append(row)
#         return triangle[rowIndex]
