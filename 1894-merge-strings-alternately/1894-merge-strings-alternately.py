class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        val = []
        for a,b in zip(word1, word2):
            val.append(a+b)
        val.append(word1[len(word2):])
        val.append(word2[len(word1):])
        return "".join(val)