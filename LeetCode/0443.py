# O(n) O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write

# O(n) O(1)
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         read = 0
#         write = 0
#         length = 0
#         for j in range(len(chars) + 1):
#             if j < len(chars) and chars[j] == chars[read]:
#                 length += 1
#                 continue

#             chars[write] = chars[read]
#             write += 1

#             if length > 1:
#                 for s in str(length):
#                     chars[write] = s
#                     write += 1

#             read = j
#             length = 1

#         return write

# O(n) O(1)
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         left = 0
#         count = 1
#         for right in range(1, len(chars) + 1):
#             if right < len(chars) and chars[right-1] == chars[right]:
#                 count += 1
#             else:
#                 chars[left] = chars[right-1]
#                 left += 1
#                 if count > 1:
#                     for s in str(count):
#                         chars[left] = s
#                         left += 1
#                 count = 1
#         return left

# O(n) O(1)
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         read = 0
#         write = 0
#         length = 0
#         for j in range(len(chars) + 1):
#             if j < len(chars) and chars[j] == chars[read]:
#                 length += 1
#                 continue
#             elif length == 1:
#                 chars[write] = chars[read]
#                 write += 1
#                 read = j
#                 length = 1
#             else:
#                 chars[write] = chars[read]
#                 write += 1
#                 for s in str(length):
#                     chars[write] = s
#                     write += 1
#                 read = j
#                 length = 1
#         return write

