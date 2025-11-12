class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = x
            z = 0
            while(x != 0):
                j = x % 10
                x = (x - j) / 10
                z = z * 10 + j
            if y == z:
                return True
            else: return False
        