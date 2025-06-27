class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o', 'u']
        i = 0
        j = len(s) - 1
        lst = list(s)
        while (i < j):
            if (lst[i].lower() not in vowels):
                i += 1
            if (lst[j].lower() not in vowels):
                j -= 1
            if ((lst[i].lower() in vowels) and (lst[j].lower() in vowels)):
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        return "".join(lst)

                


        