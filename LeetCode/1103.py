# O(n) O(n)
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        c = 1
        while candies > 0:
            res[i] += min(c, candies)
            candies -= c
            c += 1
            i = (i + 1) % num_people
        return res
