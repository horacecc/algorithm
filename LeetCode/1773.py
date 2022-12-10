# O(n) O(1)
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0 if ruleKey == 'type' else 1 if ruleKey == 'color' else 2
        res = 0
        for item in items:
            if item[i] == ruleValue:
                res += 1
        return res

# # O(n) O(n)
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         d = {'type': 0, 'color': 1, 'name': 2}
#         return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
