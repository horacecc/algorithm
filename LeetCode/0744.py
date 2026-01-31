# O(log n) O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        if target >= letters[-1]:
            return letters[0]
        
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return letters[left]

# # O(n) O(1)
# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         target_ascii = ord(target)
#         res = float('inf')
        
#         for letter in letters:
#             letter_ascii = ord(letter)
#             if letter_ascii > target_ascii:
#                 res = min(letter_ascii, res)
        
#         if res == float('inf'):
#             return letters[0]
        
#         return chr(res)

