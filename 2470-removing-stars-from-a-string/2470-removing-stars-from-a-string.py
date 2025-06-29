class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            if s[i] == "*":
                res.pop()
            else: res.append(s[i])
            i += 1
        return "".join(res)

        