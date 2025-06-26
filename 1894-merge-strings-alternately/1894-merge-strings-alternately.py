class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        val = []
        if(len(word1) <= len(word2)):
            for i in range(len(word1)):
                val.append(word1[i])
                val.append(word2[i])
        else:
            for i in range(len(word2)):
                val.append(word1[i])
                val.append(word2[i])
        val.append(word1[len(word2):])
        val.append(word2[len(word1):])
        return "".join(val)