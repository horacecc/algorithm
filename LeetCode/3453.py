# O(n log n) O(1)
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l ** 2 for x, y, l in squares)
        half_area = total_area / 2
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, l))
            events.append((y + l, 0, l))
        
        events.sort()
        
        area = 0
        width = 0
        prev_y = 0
        
        for y, is_start, l in events:
            area_gain = width * (y - prev_y)
            
            if area + area_gain >= half_area:
                return prev_y + (half_area - area) / width
            
            area += area_gain
            width += l if is_start else -l
            prev_y = y
        
        return prev_y

# # O(n) O(1)
# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         total_area = sum(l ** 2 for x, y, l in squares)
#         half_area = total_area / 2

#         lo = min(y for x, y, l in squares)
#         hi = max(y + l for x, y, l in squares)

#         def area_below(mid):
#             area = 0
#             for x, y, l in squares:
#                 if y >= mid:
#                     area += 0
#                 elif y + l <= mid:
#                     area += l ** 2
#                 else:
#                     area += l * (mid - y)
#             return area

#         for _ in range(100):
#             mid = (hi + lo) / 2
#             if area_below(mid) < half_area:
#                 lo = mid
#             else:
#                 hi = mid

#         return lo

