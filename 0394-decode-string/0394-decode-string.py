class Solution:
    def decodeString(self, s: str) -> str:
        def process(s):
            num = []
            n = 0
            res = []
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    num.append(s[i])
                elif s[i] == "[":
                    n, val = process(s[i+1 :])
                    res.append(val * int("".join(num)))
                    num = []
                    i += n + 1
                elif s[i] == "]":
                    res = "".join(res)
                    return i, res
                else:
                    res.append(s[i])
                i += 1
            return i, res
        i, res = process(s)
        res = "".join(res)
        return res
