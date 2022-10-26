# O(1) O(1)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[datetime.date(year, month, day).weekday()]
        
# # O(n) O(1)
# class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#         t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
#         if month < 3:
#             year -= 1
#         return days[(year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7]
