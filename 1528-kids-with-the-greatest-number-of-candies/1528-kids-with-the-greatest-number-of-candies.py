class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []
        for i in candies:
            if i + extraCandies < m:
                res.append(False)
            else: res.append(True)
        return res
        